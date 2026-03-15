from django.shortcuts import render
from .models import SiteProfile, Experience, Publication, Grant, TeachingItem, Award, Supervision, ServiceItem


def home(request):
    profile = SiteProfile.objects.first()
    selected_publications = Publication.objects.all().order_by('-year', 'title')[:4]
    experiences = Experience.objects.all()[:5]
    awards = Award.objects.all()[:3]
    context = {
        'profile': profile,
        'selected_publications': selected_publications,
        'experiences': experiences,
        'awards': awards,
    }
    return render(request, 'website/home.html', context)


def about(request):
    return render(request, 'website/about.html', {
        'profile': SiteProfile.objects.first(),
        'experiences': Experience.objects.all(),
    })


def research(request):
    profile = SiteProfile.objects.first()
    grants = Grant.objects.all().order_by("-year")

    context = {
        "profile": profile,
        "published_papers": Publication.objects.filter(category="published_paper").order_by("-year"),
        "media_articles": Publication.objects.filter(category="media_article").order_by("-year"),
        "book_chapters": Publication.objects.filter(category="book_chapter").order_by("-year"),
        "journal_reviewers": Publication.objects.filter(category="journal_reviewer").order_by("-year"),
        "journal_published": Publication.objects.filter(category="journal_published").order_by("-year"),
        "working_papers": Publication.objects.filter(category="working_paper").order_by("-year"),
        "grants": grants,
    }
    return render(request, "website/research.html", context)


def teaching(request):
    return render(request, 'website/teaching.html', {
        'teaching_items': TeachingItem.objects.all(),
    })


def service(request):
    items = ServiceItem.objects.all().order_by('category', 'ordering', '-title')
    return render(request, 'website/service.html', {'items': items})


def supervision_page(request):
    return render(request, 'website/supervision.html', {
        'supervisions': Supervision.objects.all(),
        'current_supervisions': Supervision.objects.filter(status='Current'),
        'completed_supervisions': Supervision.objects.filter(status='Completed'),
    })


def awards(request):
    return render(request, 'website/awards.html', {
        'awards': Award.objects.all(),
    })


def contact(request):
    return render(request, 'website/contact.html', {
        'profile': SiteProfile.objects.first(),
    })
