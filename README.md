# Sudipta Bose — Django Academic Website Starter

A modern Django starter project for rebuilding https://www.sudiptabose.com/ as a cleaner, more maintainable academic profile website.

## Why this version is better
- Modern, responsive layout
- Clear information architecture
- Database-backed content managed from Django admin
- Reusable templates and components
- Easier long-term updates for publications, grants, teaching, awards, and supervision
- SEO-ready structure and clean URLs

## Suggested pages
- Home
- Biography / About
- Research
- Publications
- Grants
- Teaching
- Supervision
- Awards
- Service
- Contact

## Quick start
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Then visit:
- http://127.0.0.1:8000/
- http://127.0.0.1:8000/admin/

## Next improvements
- Add CKEditor or Markdown for richer admin editing
- Add search and filters for publications
- Add downloadable CV and contact form email delivery
- Add Google Scholar / ORCID / Scopus integrations
- Add image optimization and sitemap
