"""
Django management command: send_reminders

Sends SMS reminders to eligible citizens who haven't applied for schemes.
Can be triggered via:
  - Manual:  python manage.py send_reminders
  - Cron:    */30 * * * * cd /path/to/project && python manage.py send_reminders
  - Filter:  python manage.py send_reminders --village="Hoskote" --state="Karnataka"

This is RULE-BASED (no AI). Logic:
1. Query MongoDB 'applications' for status='eligible_not_applied'
2. Get user phone from 'users' collection
3. Send SMS via Fast2SMS
4. Log attempt in 'sms_logs' collection
5. Mark 'reminder_sent=True' on the application record
"""

from django.core.management.base import BaseCommand
from core.reminder_service import send_reminder_to_eligible_users, calculate_village_utilization


class Command(BaseCommand):
    help = 'Send SMS reminders to eligible citizens who have not applied for schemes'

    def add_arguments(self, parser):
        parser.add_argument('--village', type=str, default=None, help='Filter by village name')
        parser.add_argument('--district', type=str, default=None, help='Filter by district name')
        parser.add_argument('--state', type=str, default=None, help='Filter by state name')
        parser.add_argument('--dry-run', action='store_true', help='Show who would receive SMS without sending')
        parser.add_argument('--stats', action='store_true', help='Show village utilization statistics only')

    def handle(self, *args, **options):
        village = options.get('village')
        district = options.get('district')
        state = options.get('state')
        dry_run = options.get('dry_run', False)
        stats_only = options.get('stats', False)

        self.stdout.write(self.style.WARNING('=' * 60))
        self.stdout.write(self.style.WARNING('  Jan Suvidha Portal — SMS Reminder System'))
        self.stdout.write(self.style.WARNING('  Rule-based | Deterministic | No AI'))
        self.stdout.write(self.style.WARNING('=' * 60))

        # Show village utilization stats
        if stats_only:
            self.show_village_stats()
            return

        # Filters
        filters = []
        if village:
            filters.append(f'Village: {village}')
        if district:
            filters.append(f'District: {district}')
        if state:
            filters.append(f'State: {state}')
        if filters:
            self.stdout.write(f'\nFilters: {", ".join(filters)}')
        else:
            self.stdout.write('\nTarget: ALL eligible users who haven\'t applied')

        if dry_run:
            self.stdout.write(self.style.WARNING('\n[DRY RUN] No SMS will be sent.\n'))

        # Send reminders
        if dry_run:
            from core.reminder_service import get_eligible_not_applied_users
            users = get_eligible_not_applied_users(village, district, state)
            self.stdout.write(f'\nFound {len(users)} user(s) who would receive reminders:\n')
            for u in users:
                self.stdout.write(
                    f'  📱 {u["name"]} | Phone: ***{u["phone"][-4:]} | '
                    f'Village: {u["village"]} | Schemes: {u["scheme_count"]}'
                )
            self.stdout.write(self.style.SUCCESS(f'\n[DRY RUN] {len(users)} SMS would be sent.'))
        else:
            self.stdout.write('\nSending reminders...\n')
            result = send_reminder_to_eligible_users(village, district, state)

            self.stdout.write(f'\n📊 Results:')
            self.stdout.write(f'  Total users targeted: {result["total_users"]}')
            self.stdout.write(f'  SMS sent:             {result["sms_sent"]}')
            self.stdout.write(f'  SMS simulated:        {result["sms_simulated"]}')
            self.stdout.write(f'  SMS failed:           {result["sms_failed"]}')

            if result['sms_simulated'] > 0:
                self.stdout.write(self.style.WARNING(
                    '\n⚠️  SMS simulated (FAST2SMS_API_KEY not set). '
                    'Set the API key in environment to send real SMS.'
                ))

            self.stdout.write(self.style.SUCCESS(f'\n✅ {result["message"]}'))

    def show_village_stats(self):
        """Display village-wise utilization statistics."""
        stats = calculate_village_utilization()

        if not stats:
            self.stdout.write(self.style.WARNING('\nNo application data found.'))
            return

        self.stdout.write(f'\n{"Village":<20} {"District":<15} {"Eligible":>8} {"Applied":>8} {"Gap":>6} {"Rate":>6} {"Status":<10}')
        self.stdout.write('-' * 80)

        for s in stats:
            gap = s['eligible_users'] - s['applied_users']
            status = '🔴 CRITICAL' if s['is_critical'] else '🟢 OK'
            self.stdout.write(
                f'{s["village"]:<20} {s["district"]:<15} {s["eligible_users"]:>8} '
                f'{s["applied_users"]:>8} {gap:>6} {s["utilization_rate"]:>5}% {status:<10}'
            )

        critical = [s for s in stats if s['is_critical']]
        self.stdout.write(f'\n📍 Total areas: {len(stats)} | 🔴 Critical: {len(critical)}')
