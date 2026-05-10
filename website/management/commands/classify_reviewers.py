from django.core.management.base import BaseCommand
from website.models import Publication

class Command(BaseCommand):
    help = 'Classify journal_reviewer Publication entries into journal_type using heuristics'

    def handle(self, *args, **options):
        qs = Publication.objects.filter(category='journal_reviewer')
        count = 0
        for p in qs:
            if p.journal_type:
                continue
            name = (p.journal_or_source or '').lower()
            new_type = None
            if 'account' in name:
                new_type = 'accounting'
            elif 'finance' in name:
                new_type = 'finance'
            elif 'econom' in name:
                new_type = 'economics'
            elif 'manage' in name:
                new_type = 'management'
            elif 'conference' in name or 'ad-hoc' in name or 'ad hoc' in name:
                new_type = 'conference_reviewer'
            if new_type:
                p.journal_type = new_type
                p.save(update_fields=['journal_type'])
                count += 1
                self.stdout.write(f"Set journal_type={new_type} for Publication id={p.id} title='{p.title}'")
        self.stdout.write(f"Classification complete: {count} updated")
