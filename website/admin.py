from django.contrib import admin
from .models import SiteProfile, Experience, Publication, Grant, TeachingItem, TeachingResource, Award, Supervision, ServiceItem, GalleryPhoto


@admin.register(SiteProfile)
class SiteProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'title', 'institution')


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('role', 'organization', 'start_date', 'end_date', 'ordering')
    list_editable = ('ordering',)


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'category', 'featured', 'featured_order', 'ft50', 'journal_type', 'rank', 'abs_rank', 'sjr_rank', 'citation_count')
    list_editable = ('featured', 'featured_order', 'ft50', 'journal_type', 'rank', 'abs_rank', 'sjr_rank', 'citation_count')
    list_filter = ('featured', 'ft50', 'journal_type', 'category', 'year', 'rank', 'abs_rank', 'sjr_rank')
    search_fields = ('title', 'authors', 'journal_or_source', 'book_title', 'conference_name')

    fieldsets = (
        ('Core', {
            'fields': ('title', 'authors', 'year', 'category', 'featured', 'featured_order', 'link', 'abstract', 'abstract_image')
        }),
        ('Journal / Source', {
            'fields': ('journal_or_source', 'volume', 'issue', 'pages', 'doi')
        }),
        ('Rankings', {
            'fields': ('ft50', 'journal_type', 'rank', 'abs_rank', 'sjr_rank', 'citation_count'),
            'description': 'Tick FT50 for Financial Times 50 journals. Select a journal type for reviewer entries. ABDC rank (A*, A, B, C) · ABS rank (1–4*) · SJR quartile (Q1–Q4). For book chapters, the ABDC/rank field stores the APSA rank.'
        }),
        ('Book Chapter', {
            'fields': ('editors', 'book_title', 'publisher', 'publisher_location'),
            'classes': ('collapse',),
        }),
        ('Conference Paper', {
            'fields': ('conference_name', 'conference_location'),
            'classes': ('collapse',),
        }),
        ('APA7 Override', {
            'fields': ('reference_apa7',),
            'classes': ('collapse',),
            'description': 'Optional: paste a fully formatted APA7 reference to override the auto-generated one.'
        }),
    )


@admin.register(Grant)
class GrantAdmin(admin.ModelAdmin):
    list_display = ('title', 'funder', 'year', 'amount')
    list_filter = ('year', 'funder')


@admin.register(TeachingItem)
class TeachingItemAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'institution', 'level', 'start_year', 'end_year', 'ordering')
    list_editable = ('ordering',)


@admin.register(TeachingResource)
class TeachingResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'resource_type', 'course', 'ordering')
    list_editable = ('ordering',)
    list_filter = ('resource_type', 'course')


@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'issuer')
    list_filter = ('year',)


@admin.register(Supervision)
class SupervisionAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'degree', 'status', 'role', 'current_position', 'completed_year', 'ordering')
    list_editable = ('ordering',)
    fields = ('student_name', 'degree', 'status', 'role', 'topic', 'current_position', 'completed_year', 'ordering')


@admin.register(ServiceItem)
class ServiceItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'role', 'organization', 'year_range', 'category', 'ordering')
    list_editable = ('ordering',)


@admin.register(GalleryPhoto)
class GalleryPhotoAdmin(admin.ModelAdmin):
    list_display = ('caption', 'year', 'ordering')
    list_editable = ('ordering',)
