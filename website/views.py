from django.shortcuts import render
from .models import SiteProfile, Experience, Publication, Grant, TeachingItem, Award, Supervision


def home(request):
    profile = SiteProfile.objects.first()
    featured_publications = Publication.objects.filter(featured=True)[:4]
    experiences = Experience.objects.all()[:5]
    awards = Award.objects.all()[:3]
    context = {
        'profile': profile,
        'featured_publications': featured_publications,
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
    return render(request, 'website/research.html', {
        'profile': SiteProfile.objects.first(),
        'publications': Publication.objects.all(),
        'grants': Grant.objects.all(),
    })


def teaching(request):
    return render(request, 'website/teaching.html', {
        'teaching_items': TeachingItem.objects.all(),
        'supervisions': Supervision.objects.all(),
    })


def awards(request):
    return render(request, 'website/awards.html', {
        'awards': Award.objects.all(),
    })


def contact(request):
    return render(request, 'website/contact.html', {
        'profile': SiteProfile.objects.first(),
    })
