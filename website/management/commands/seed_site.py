from django.core.management.base import BaseCommand
from website.models import SiteProfile, Experience, Publication, Grant, TeachingItem, Award, Supervision


class Command(BaseCommand):
    help = 'Seed the site with starter content based on the existing profile.'

    def handle(self, *args, **options):
        SiteProfile.objects.all().delete()
        Experience.objects.all().delete()
        Publication.objects.all().delete()
        Grant.objects.all().delete()
        TeachingItem.objects.all().delete()
        Award.objects.all().delete()
        Supervision.objects.all().delete()

        SiteProfile.objects.create(
            full_name='Dr Sudipta Bose',
            title='Associate Professor of Accounting',
            institution='The University of Newcastle',
            bio=(
                'Dr Sudipta Bose is an academic in accounting whose work spans capital markets, sustainable finance, '
                'climate-related disclosure, governance, and machine learning. This redesigned site presents his profile '
                'with a cleaner structure focused on research impact, teaching, supervision, and professional service.'
            ),
            research_interests='Capital markets, sustainable finance, climate change, carbon emissions, assurance, biodiversity, corporate governance, machine learning',
            skills='STATA, R, Python, Power BI, LaTeX',
            email='contact@example.com',
            scholar_url='https://scholar.google.com/',
            orcid_url='https://orcid.org/',
            linkedin_url='https://www.linkedin.com/'
        )

        experiences = [
            ('Associate Professor', 'The University of Newcastle', 'November 2025', 'Present'),
            ('Senior Lecturer', 'The University of Newcastle', 'January 2019', 'October 2025'),
            ('Visiting Researcher', 'The University of Sydney', 'July 2023', 'December 2023'),
            ('Lecturer', 'The University of Newcastle', '2017', '2018'),
            ('Teaching & Research', 'UNSW Sydney', '2010', '2016'),
        ]
        for idx, item in enumerate(experiences, start=1):
            Experience.objects.create(role=item[0], organization=item[1], start_date=item[2], end_date=item[3], ordering=idx)

        publications = [
            ('Climate disclosure and firm outcomes', 'Sudipta Bose et al.', 2025, 'Journal of Corporate Finance', 'journal', True),
            ('Sustainability assurance and market effects', 'Sudipta Bose et al.', 2024, 'Accounting & Finance', 'journal', True),
            ('Machine learning in accounting research', 'Sudipta Bose et al.', 2024, 'Working Paper Series', 'working', False),
            ('Carbon emissions reporting and governance', 'Sudipta Bose et al.', 2023, 'British Accounting Review', 'journal', True),
        ]
        for title, authors, year, source, category, featured in publications:
            Publication.objects.create(title=title, authors=authors, year=year, journal_or_source=source, category=category, featured=featured)

        Grant.objects.create(title='Climate-related disclosure research project', funder='AASB', amount='TBD', year=2024, summary='Research on reporting standards and disclosure quality.')
        Grant.objects.create(title='Sustainable finance and biodiversity reporting', funder='ADB', amount='TBD', year=2023, summary='Research focused on sustainability and finance intersections.')

        TeachingItem.objects.create(course_name='Corporate Financial Reporting and Analysis', institution='The University of Newcastle', level='Postgraduate', ordering=1)
        TeachingItem.objects.create(course_name='Management Accounting', institution='The University of Newcastle', level='Undergraduate', ordering=2)
        TeachingItem.objects.create(course_name='Foundations of Financial Accounting', institution='UNSW Sydney', level='Undergraduate', ordering=3)

        Award.objects.create(title='Excellence Award for Research Supervision', year=2023, issuer='CHSF')
        Award.objects.create(title='Excellence Award for Student Experience', year=2023, issuer='CHSF')
        Award.objects.create(title='Teaching Excellence Award', year=2019, issuer='Faculty of Business and Law')

        Supervision.objects.create(student_name='Example PhD Candidate', degree='PhD', status='Current', role='Principal Supervisor', topic='Sustainability reporting', ordering=1)
        Supervision.objects.create(student_name='Example MPhil Candidate', degree='MPhil', status='Current', role='Co-Supervisor', topic='Corporate governance', ordering=2)

        self.stdout.write(self.style.SUCCESS('Starter content created.'))
