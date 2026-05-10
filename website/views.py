from django.shortcuts import render
from .models import SiteProfile, Experience, Publication, Grant, TeachingItem, TeachingResource, Award, Supervision, ServiceItem, GalleryPhoto


def home(request):
    profile = SiteProfile.objects.first()
    featured_publications = Publication.objects.filter(featured=True).order_by('featured_order', '-year')[:4]
    experiences = Experience.objects.all()[:5]
    awards = Award.objects.all()[:3]
    photos = GalleryPhoto.objects.all()
    context = {
        'profile': profile,
        'featured_publications': featured_publications,
        'experiences': experiences,
        'awards': awards,
        'photos': photos,
    }
    return render(request, 'website/home.html', context)


def about(request):
    return render(request, 'website/about.html', {
        'profile': SiteProfile.objects.first(),
        'experiences': Experience.objects.all(),
    })


def research(request):
    profile = SiteProfile.objects.first()
    featured = Publication.objects.filter(featured=True).order_by('featured_order', '-year')
    published = Publication.objects.filter(category="published_paper").order_by("-year")
    conference = Publication.objects.filter(category="conference_paper").order_by("-year")
    media = Publication.objects.filter(category="media_article").order_by("-year")
    books = Publication.objects.filter(category="book_chapter").order_by("-year")
    journal_publish = Publication.objects.filter(category="journal_published").order_by("-year")
    working = Publication.objects.filter(category="working_paper").order_by("-year")

    # Group journal reviewers by journal_type
    jr_qs = Publication.objects.filter(category="journal_reviewer").order_by('journal_type', '-year')
    # Start groups for explicit types
    journal_reviewer_groups = []
    grouped = {}
    for key, label in Publication.JOURNAL_TYPE_CHOICES:
        grouped[key] = list(jr_qs.filter(journal_type=key))

    # Heuristic classification for entries without journal_type
    untyped = [p for p in jr_qs if not p.journal_type]
    for p in untyped:
        name = (p.journal_or_source or '').lower()
        classified = False
        if 'account' in name:
            grouped.setdefault('accounting', []).append(p); classified = True
        elif 'finance' in name:
            grouped.setdefault('finance', []).append(p); classified = True
        elif 'econom' in name:
            grouped.setdefault('economics', []).append(p); classified = True
        elif 'manage' in name:
            grouped.setdefault('management', []).append(p); classified = True
        elif 'conference' in name or 'ad-hoc' in name or 'ad hoc' in name:
            grouped.setdefault('conference_reviewer', []).append(p); classified = True
        if not classified:
            grouped.setdefault('other', []).append(p)

    # Build final groups in the specified order, include 'Other' last if present
    for key, label in Publication.JOURNAL_TYPE_CHOICES:
        items = grouped.get(key, [])
        if items:
            journal_reviewer_groups.append({'key': key, 'label': label, 'items': items})
    if grouped.get('other'):
        journal_reviewer_groups.append({'key': 'other', 'label': 'Other / Unspecified', 'items': grouped.get('other')})

    context = {
        "profile": profile,
        "featured_papers": featured,
        "published_papers": published,
        "conference_papers": conference,
        "media_articles": media,
        "book_chapters": books,
        "journal_reviewers": jr_qs,
        "journal_reviewer_groups": journal_reviewer_groups,
        "journal_published": journal_publish,
        "working_papers": working,
    }
    return render(request, "website/research.html", context)


def grants_page(request):
    grants = Grant.objects.all().order_by("-year")
    earliest = grants.last()
    latest = grants.first()
    return render(request, "website/grants.html", {"grants": grants, "earliest": earliest, "latest": latest})


def teaching(request):
    resources = TeachingResource.objects.select_related('course').all()
    resource_groups = []
    for key, label in TeachingResource.RESOURCE_TYPE_CHOICES:
        grouped_items = resources.filter(resource_type=key)
        if grouped_items.exists():
            resource_groups.append({'key': key, 'label': label, 'items': grouped_items})

    # Order teaching items by institution then ordering so frontend can group by institution
    teaching_items = TeachingItem.objects.all().order_by('institution', 'ordering', 'course_name')

    return render(request, 'website/teaching.html', {
        'teaching_items': teaching_items,
        'resources': resources,
        'resource_types': TeachingResource.RESOURCE_TYPE_CHOICES,
        'resource_groups': resource_groups,
    })


def service(request):
    items = ServiceItem.objects.all().order_by('ordering')
    return render(request, 'website/service.html', {'items': items})


def supervision_page(request):
    return render(request, 'website/supervision.html', {
        'supervisions': Supervision.objects.all(),
        'current_supervisions': Supervision.objects.filter(status__iexact='Current'),
        'completed_supervisions': Supervision.objects.filter(status__iexact='Completed'),
    })


def awards(request):
    return render(request, 'website/awards.html', {
        'awards': Award.objects.all(),
    })


def contact(request):
    return render(request, 'website/contact.html', {
        'profile': SiteProfile.objects.first(),
    })
