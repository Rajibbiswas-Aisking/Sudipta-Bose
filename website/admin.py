from django.contrib import admin
from .models import SiteProfile, Experience, Publication, Grant, TeachingItem, Award, Supervision, ServiceItem, GalleryPhoto


@admin.register(SiteProfile)
class SiteProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'title', 'institution')


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('role', 'organization', 'start_date', 'end_date', 'ordering')
    list_editable = ('ordering',)


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'category', 'abstract_image')
    list_filter = ('category', 'year')
    search_fields = ('title', 'authors', 'journal_or_source')
    fields = ('title', 'authors', 'year', 'category', 'journal_or_source', 'abstract', 'abstract_image', 'link')


@admin.register(Grant)
class GrantAdmin(admin.ModelAdmin):
    list_display = ('title', 'funder', 'year', 'amount')
    list_filter = ('year', 'funder')


@admin.register(TeachingItem)
class TeachingItemAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'institution', 'level', 'ordering')
    list_editable = ('ordering',)


@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'issuer')
    list_filter = ('year',)


@admin.register(Supervision)
class SupervisionAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'degree', 'status', 'role', 'ordering')
    list_editable = ('ordering',)


@admin.register(ServiceItem)
class ServiceItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'role', 'organization', 'year_range', 'category', 'ordering')
    list_editable = ('ordering',)


@admin.register(GalleryPhoto)
class GalleryPhotoAdmin(admin.ModelAdmin):
    list_display = ('caption', 'year', 'ordering')
    list_editable = ('ordering',)
