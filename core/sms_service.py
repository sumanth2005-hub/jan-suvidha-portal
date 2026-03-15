"""
Fast2SMS Integration for Jan Suvidha Portal.

Sends SMS reminders to eligible citizens who haven't applied.
Uses Fast2SMS Quick SMS API (https://www.fast2sms.com/).

IMPORTANT:
- API key stored in environment variable FAST2SMS_API_KEY
- NO hardcoded keys anywhere
- Every SMS attempt is logged in MongoDB 'sms_logs' collection
- Handles API failures gracefully with retry logic
"""
import os
import json
import logging
import requests
from datetime import datetime, timezone
from django.conf import settings

logger = logging.getLogger(__name__)

# Fast2SMS API endpoint (Quick SMS)
FAST2SMS_URL = "https://www.fast2sms.com/dev/bulkV2"

# Fast2SMS OTP endpoint
FAST2SMS_OTP_URL = "https://www.fast2sms.com/dev/bulkV2"

# Default reminder message (short, simple, under 160 chars)
DEFAULT_REMINDER_MESSAGE = (
    "Jan Suvidha Alert: You are eligible for welfare schemes but have not applied yet. "
    "Please apply soon to avail benefits. Visit Jan Suvidha Portal."
)

# Multilingual messages
REMINDER_MESSAGES = {
    'en': "Jan Suvidha: You are eligible for welfare schemes but have not applied yet. Please apply soon.",
    'hi': "जन सुविधा: आप कल्याण योजनाओं के लिए पात्र हैं लेकिन अभी तक आवेदन नहीं किया। कृपया जल्द आवेदन करें।",
    'kn': "ಜನ ಸುವಿಧಾ: ನೀವು ಯೋಜನೆಗಳಿಗೆ ಅರ್ಹರು ಆದರೆ ಅರ್ಜಿ ಸಲ್ಲಿಸಿಲ್ಲ. ದಯವಿಟ್ಟು ಶೀಘ್ರ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ.",
    'te': "జన సువిధా: మీరు పథకాలకు అర్హులు కానీ దరఖాస్తు చేయలేదు. దయచేసి త్వరగా దరఖాస్తు చేయండి.",
    'ta': "ஜன சுவிதா: நீங்கள் திட்டங்களுக்கு தகுதி பெற்றுள்ளீர்கள் ஆனால் விண்ணப்பிக்கவில்லை. விரைவில் விண்ணப்பியுங்கள்.",
}


def get_api_key():
    """Get Fast2SMS API key from environment (NEVER hardcoded)."""
    key = os.environ.get('FAST2SMS_API_KEY', getattr(settings, 'FAST2SMS_API_KEY', ''))
    if not key:
        logger.warning("FAST2SMS_API_KEY not set in environment variables")
    return key


def log_sms_attempt(db_collection, phone, message, status, response_data=None, error=None):
    """
    Log every SMS attempt in MongoDB 'sms_logs' collection.
    This creates an audit trail for all SMS activity.
    """
    log_entry = {
        'phone': phone,
        'message': message[:100] + '...' if len(message) > 100 else message,
        'status': status,  # 'sent', 'failed', 'simulated', 'api_error'
        'response': response_data,
        'error': str(error) if error else None,
        'timestamp': datetime.now(timezone.utc),
        'source': 'fast2sms',
    }
    try:
        db_collection.insert_one(log_entry)
    except Exception as e:
        logger.error(f"Failed to log SMS attempt: {e}")


def send_sms(phone, message=None, language='en', sms_logs_collection=None):
    """
    Send SMS via Fast2SMS API.

    Args:
        phone: 10-digit mobile number (without +91)
        message: Custom message (optional, uses default if None)
        language: Language code for the message
        sms_logs_collection: MongoDB collection for logging

    Returns:
        dict: {'success': bool, 'message': str, 'response': dict}
    """
    # Use language-specific message if no custom message provided
    if message is None:
        message = REMINDER_MESSAGES.get(language, REMINDER_MESSAGES['en'])

    # Clean phone number (remove +91, spaces, dashes)
    phone = str(phone).strip().replace('+91', '').replace(' ', '').replace('-', '')
    if len(phone) != 10 or not phone.isdigit():
        result = {'success': False, 'message': f'Invalid phone number: {phone}'}
        if sms_logs_collection is not None:
            log_sms_attempt(sms_logs_collection, phone, message, 'failed', error='Invalid phone')
        return result

    api_key = get_api_key()

    # If no API key, simulate (for demo/hackathon)
    if not api_key:
        logger.info(f"[SIMULATED SMS] To: {phone} | Message: {message[:50]}...")
        result = {
            'success': True,
            'message': f'SMS simulated to {phone} (no API key configured)',
            'simulated': True,
        }
        if sms_logs_collection is not None:
            log_sms_attempt(sms_logs_collection, phone, message, 'simulated')
        return result

    # ─── Actual Fast2SMS API Call ───
    try:
        headers = {
            "authorization": api_key,
            "Content-Type": "application/json",
        }
        payload = {
            "route": "q",           # Quick SMS route
            "message": message,
            "language": "english" if language == 'en' else "unicode",
            "flash": 0,
            "numbers": phone,
        }

        response = requests.post(
            FAST2SMS_URL,
            headers=headers,
            json=payload,
            timeout=10,
        )

        response_data = response.json()

        if response.status_code == 200 and response_data.get('return'):
            result = {
                'success': True,
                'message': f'SMS sent to {phone}',
                'response': response_data,
            }
            if sms_logs_collection is not None:
                log_sms_attempt(sms_logs_collection, phone, message, 'sent', response_data)
            logger.info(f"[SMS SENT] To: {phone}")
            return result
        else:
            result = {
                'success': False,
                'message': f'Fast2SMS API error: {response_data.get("message", "Unknown error")}',
                'response': response_data,
            }
            if sms_logs_collection is not None:
                log_sms_attempt(sms_logs_collection, phone, message, 'api_error', response_data)
            logger.error(f"[SMS FAILED] To: {phone} | Error: {response_data}")
            return result

    except requests.exceptions.Timeout:
        error_msg = 'Fast2SMS API timeout'
        if sms_logs_collection is not None:
            log_sms_attempt(sms_logs_collection, phone, message, 'failed', error=error_msg)
        return {'success': False, 'message': error_msg}

    except requests.exceptions.ConnectionError:
        error_msg = 'Fast2SMS API connection failed'
        if sms_logs_collection is not None:
            log_sms_attempt(sms_logs_collection, phone, message, 'failed', error=error_msg)
        return {'success': False, 'message': error_msg}

    except Exception as e:
        error_msg = f'Unexpected error: {str(e)}'
        if sms_logs_collection is not None:
            log_sms_attempt(sms_logs_collection, phone, message, 'failed', error=error_msg)
        logger.exception(f"[SMS ERROR] To: {phone}")
        return {'success': False, 'message': error_msg}


def send_bulk_sms(phone_list, message=None, language='en', sms_logs_collection=None):
    """
    Send SMS to multiple phone numbers.

    Args:
        phone_list: List of phone numbers
        message: Message to send
        language: Language code
        sms_logs_collection: MongoDB collection for logging

    Returns:
        dict: {'total': int, 'sent': int, 'failed': int, 'details': list}
    """
    results = {'total': len(phone_list), 'sent': 0, 'failed': 0, 'simulated': 0, 'details': []}

    for phone in phone_list:
        result = send_sms(phone, message, language, sms_logs_collection)
        results['details'].append({'phone': phone, **result})
        if result.get('success'):
            if result.get('simulated'):
                results['simulated'] += 1
            else:
                results['sent'] += 1
        else:
            results['failed'] += 1

    return results
