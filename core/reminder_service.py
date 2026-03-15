"""
Rule-Based Reminder Service for Jan Suvidha Portal.

This module contains DETERMINISTIC, rule-based logic (NO AI) for:
1. Finding eligible users who haven't applied
2. Calculating per-village/area utilization
3. Triggering SMS reminders via Fast2SMS

IMPORTANT:
- This is NOT AI-driven — it's purely rule-based and deterministic
- Uses MongoDB queries to determine eligibility vs application status
- Reminders are triggered by:
  (a) Admin manually from dashboard (api_send_reminder)
  (b) Periodic cron job (management command send_reminders)
"""
import logging
from datetime import datetime, timezone
from bson import ObjectId
from .db import get_collection
from .sms_service import send_sms, send_bulk_sms, REMINDER_MESSAGES

logger = logging.getLogger(__name__)


def get_eligible_not_applied_users(village=None, district=None, state=None):
    """
    Find all users who are eligible for at least one scheme
    but have NOT applied for it.

    Data flow:
    1. Query 'applications' collection for status = 'eligible_not_applied'
    2. Join with 'users' collection to get phone numbers
    3. Optionally filter by village/district/state

    Returns:
        list of dicts: [{user_id, phone, name, language, village, scheme_ids, scheme_names}]
    """
    apps_col = get_collection('applications')
    users_col = get_collection('users')

    # Step 1: Find all eligible-but-not-applied records
    app_query = {'status': 'eligible_not_applied'}
    eligible_apps = list(apps_col.find(app_query))

    # Step 2: Group by user
    user_scheme_map = {}
    for app in eligible_apps:
        uid = str(app.get('user_id', ''))
        if uid not in user_scheme_map:
            user_scheme_map[uid] = {
                'user_id': uid,
                'scheme_ids': [],
                'scheme_names': [],
                'reminder_already_sent': [],
            }
        user_scheme_map[uid]['scheme_ids'].append(app.get('scheme_id', ''))
        user_scheme_map[uid]['scheme_names'].append(app.get('scheme_name', ''))
        user_scheme_map[uid]['reminder_already_sent'].append(app.get('reminder_sent', False))

    # Step 3: Fetch user details and apply location filters
    result = []
    for uid, data in user_scheme_map.items():
        try:
            user = users_col.find_one({'_id': ObjectId(uid)}) if len(uid) == 24 else None
        except Exception:
            user = None

        if not user:
            continue

        # Apply location filters
        if village and user.get('village', '').lower() != village.lower():
            continue
        if district and user.get('district', '').lower() != district.lower():
            continue
        if state and user.get('state', '').lower() != state.lower():
            continue

        # Check if ALL reminders already sent
        all_sent = all(data['reminder_already_sent'])
        if all_sent:
            continue  # Skip users who already received reminders

        result.append({
            'user_id': uid,
            'phone': user.get('phone', ''),
            'name': user.get('name', 'Citizen'),
            'language': user.get('language', 'en'),
            'village': user.get('village', 'Unknown'),
            'district': user.get('district', ''),
            'state': user.get('state', ''),
            'scheme_count': len(data['scheme_ids']),
            'scheme_ids': data['scheme_ids'],
            'scheme_names': data['scheme_names'],
        })

    return result


def calculate_village_utilization():
    """
    Calculate per-village utilization metrics.

    For each village/area:
    - Eligible Users Count
    - Applied Users Count
    - Not Applied Count = Eligible − Applied
    - Utilization Rate = Applied / Eligible × 100

    Returns:
        list of dicts sorted by utilization_rate (lowest first)
    """
    apps_col = get_collection('applications')
    users_col = get_collection('users')

    all_apps = list(apps_col.find({}))

    # Group applications by user → village
    village_stats = {}
    user_cache = {}

    for app in all_apps:
        uid = str(app.get('user_id', ''))

        # Cache user lookups
        if uid not in user_cache:
            try:
                user = users_col.find_one({'_id': ObjectId(uid)}) if len(uid) == 24 else None
            except Exception:
                user = None
            user_cache[uid] = user

        user = user_cache[uid]
        if not user:
            continue

        village = user.get('village', 'Unknown')
        district = user.get('district', '')
        state = user.get('state', '')
        key = f"{village}|{district}|{state}"

        if key not in village_stats:
            village_stats[key] = {
                'village': village,
                'district': district,
                'state': state,
                'eligible_users': set(),
                'applied_users': set(),
                'not_applied_users': set(),
                'total_eligible': 0,
                'total_applied': 0,
            }

        village_stats[key]['total_eligible'] += 1
        village_stats[key]['eligible_users'].add(uid)

        if app.get('status') == 'applied':
            village_stats[key]['total_applied'] += 1
            village_stats[key]['applied_users'].add(uid)
        else:
            village_stats[key]['not_applied_users'].add(uid)

    # Calculate rates and convert sets to counts
    result = []
    for key, stats in village_stats.items():
        eligible_count = len(stats['eligible_users'])
        applied_count = len(stats['applied_users'])
        not_applied_count = len(stats['not_applied_users'] - stats['applied_users'])
        utilization = round((applied_count / eligible_count * 100) if eligible_count > 0 else 0, 1)

        result.append({
            'village': stats['village'],
            'district': stats['district'],
            'state': stats['state'],
            'eligible_users': eligible_count,
            'applied_users': applied_count,
            'not_applied_users': not_applied_count,
            'total_eligible_schemes': stats['total_eligible'],
            'total_applied_schemes': stats['total_applied'],
            'utilization_rate': utilization,
            'is_critical': utilization < 50,  # Critical if < 50% utilization
        })

    # Sort by utilization rate (lowest first = most critical)
    result.sort(key=lambda x: x['utilization_rate'])
    return result


def send_reminder_to_eligible_users(village=None, district=None, state=None):
    """
    Main reminder trigger function.

    Logic (rule-based, deterministic):
    1. Find all users who are eligible but haven't applied
    2. For each user:
       a. Get their phone number from MongoDB
       b. Get their preferred language
       c. Send SMS via Fast2SMS in their language
       d. Log the SMS attempt in MongoDB
       e. Mark the application as 'reminder_sent = True'

    Args:
        village: Optional filter by village
        district: Optional filter by district
        state: Optional filter by state

    Returns:
        dict: Summary of reminders sent
    """
    sms_logs = get_collection('sms_logs')
    apps_col = get_collection('applications')

    # Step 1: Get eligible users who haven't applied
    users = get_eligible_not_applied_users(village, district, state)

    if not users:
        return {
            'success': True,
            'total_users': 0,
            'sms_sent': 0,
            'sms_failed': 0,
            'sms_simulated': 0,
            'message': 'No eligible users found who need reminders.',
        }

    # Step 2: Send SMS to each user
    sent = 0
    failed = 0
    simulated = 0
    details = []

    for user in users:
        phone = user.get('phone', '')
        language = user.get('language', 'en')
        name = user.get('name', 'Citizen')

        # Personalize message slightly
        message = REMINDER_MESSAGES.get(language, REMINDER_MESSAGES['en'])

        # Step 3: Send SMS
        result = send_sms(
            phone=phone,
            message=message,
            language=language,
            sms_logs_collection=sms_logs,
        )

        # Step 4: Update application records (mark reminder_sent)
        if result.get('success'):
            for scheme_id in user.get('scheme_ids', []):
                apps_col.update_many(
                    {
                        'user_id': user['user_id'],
                        'scheme_id': scheme_id,
                        'status': 'eligible_not_applied',
                    },
                    {
                        '$set': {
                            'reminder_sent': True,
                            'reminder_sent_at': datetime.now(timezone.utc),
                            'reminder_method': 'sms_fast2sms',
                        }
                    }
                )

            if result.get('simulated'):
                simulated += 1
            else:
                sent += 1
        else:
            failed += 1

        details.append({
            'name': name,
            'phone': phone[-4:].rjust(len(phone), '*'),  # Mask phone
            'village': user.get('village', ''),
            'schemes': user.get('scheme_count', 0),
            'status': 'sent' if result['success'] else 'failed',
        })

    return {
        'success': True,
        'total_users': len(users),
        'sms_sent': sent,
        'sms_failed': failed,
        'sms_simulated': simulated,
        'message': f'Reminders processed for {len(users)} citizens. Sent: {sent}, Simulated: {simulated}, Failed: {failed}.',
        'details': details,
    }


def get_sms_logs(limit=50):
    """
    Get recent SMS log entries from MongoDB.

    Returns:
        list of dicts: Recent SMS attempts
    """
    sms_logs = get_collection('sms_logs')
    logs = list(sms_logs.find({}).sort('timestamp', -1).limit(limit))

    for log in logs:
        log['_id'] = str(log['_id'])
        if isinstance(log.get('timestamp'), datetime):
            log['timestamp'] = log['timestamp'].isoformat()

    return logs
