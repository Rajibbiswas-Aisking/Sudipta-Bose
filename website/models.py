from django.db import models


class SiteProfile(models.Model):
    full_name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to="profile_photos/", blank=True, null=True)
    title = models.CharField(max_length=200)
    institution = models.CharField(max_length=200, blank=True)
    bio = models.TextField()
    research_interests = models.TextField(blank=True)
    skills = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    scholar_url = models.URLField(blank=True)
    orcid_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    researchgate_url = models.URLField(blank=True)
    ssrn_url = models.URLField(blank=True)
    scopus_url = models.URLField(blank=True)
    webofscience_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    bluesky_url = models.URLField(blank=True)
    cssn_url = models.URLField(blank=True)
    education = models.TextField(blank=True)
    professional_education = models.TextField(blank=True)
    positions = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Site Profile'
        verbose_name_plural = 'Site Profile'

    def __str__(self):
        return self.full_name


class Experience(models.Model):
    role = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50, blank=True)
    summary = models.TextField(blank=True)
    ordering = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['ordering']

    def __str__(self):
        return f"{self.role} — {self.organization}"


class Publication(models.Model):
    CATEGORY_CHOICES = [
        ("published_paper", "Published Paper"),
        ("media_article", "Media Article"),
        ("book_chapter", "Book Chapter"),
        ("journal_reviewer", "Journal Reviewer"),
        ("journal_published", "Journal Published"),
        ("working_paper", "Working Paper"),
    ]

    title = models.CharField(max_length=300)
    authors = models.CharField(max_length=300, blank=True)
    year = models.PositiveIntegerField()
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    journal_or_source = models.CharField(max_length=300, blank=True)
    rank = models.CharField(max_length=20, blank=True, help_text='e.g. A*, A, B, C (ABDC) or A (APSA)')
    citation_count = models.PositiveIntegerField(null=True, blank=True, help_text='Google Scholar citation count')
    abstract = models.TextField(blank=True)
    abstract_image = models.ImageField(upload_to="abstract_images/", blank=True, null=True)
    link = models.URLField(blank=True)

    class Meta:
        ordering = ['-year', 'title']

    def __str__(self):
        return f"{self.year} — {self.title}"


class Grant(models.Model):
    title = models.CharField(max_length=250)
    funder = models.CharField(max_length=200)
    amount = models.CharField(max_length=100, blank=True)
    year = models.PositiveIntegerField()
    summary = models.TextField(blank=True)

    class Meta:
        ordering = ['-year', 'title']

    def __str__(self):
        return self.title


class TeachingItem(models.Model):
    course_name = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    level = models.CharField(max_length=100, blank=True)
    summary = models.TextField(blank=True)
    ordering = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['ordering', 'course_name']

    def __str__(self):
        return self.course_name


class TeachingResource(models.Model):
    RESOURCE_TYPE_CHOICES = [
        ('reading_list', 'Reading List'),
        ('lecture_notes', 'Lecture Notes'),
        ('template', 'Template'),
        ('external_tool', 'External Tool'),
        ('assessment_guide', 'Assessment Guide'),
    ]

    title = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    resource_type = models.CharField(max_length=30, choices=RESOURCE_TYPE_CHOICES)
    file = models.FileField(upload_to='teaching_resources/', blank=True, null=True)
    url = models.URLField(blank=True)
    course = models.ForeignKey(TeachingItem, on_delete=models.SET_NULL, null=True, blank=True, related_name='resources')
    ordering = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['ordering', 'resource_type', 'title']

    def __str__(self):
        return self.title


class Award(models.Model):
    title = models.CharField(max_length=250)
    year = models.PositiveIntegerField()
    issuer = models.CharField(max_length=200, blank=True)
    summary = models.TextField(blank=True)

    class Meta:
        ordering = ['-year', 'title']

    def __str__(self):
        return f"{self.year} — {self.title}"


class Supervision(models.Model):
    student_name = models.CharField(max_length=200)
    degree = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    role = models.CharField(max_length=100, help_text='Principal supervisor / Co-supervisor')
    topic = models.CharField(max_length=250, blank=True)
    ordering = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['ordering', 'student_name']

    def __str__(self):
        return f"{self.student_name} ({self.degree})"


class ServiceItem(models.Model):
    title = models.CharField(max_length=250)
    role = models.CharField(max_length=200, blank=True)
    organization = models.CharField(max_length=200, blank=True)
    year_range = models.CharField(max_length=100, blank=True, help_text='e.g. 2021–Present')
    category = models.CharField(max_length=100, blank=True, help_text='e.g. Editorial, Conference, Grant Review')
    ordering = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['ordering', '-title']

    def __str__(self):
        return self.title


class GalleryPhoto(models.Model):
    image = models.ImageField(upload_to='gallery/')
    caption = models.CharField(max_length=300, blank=True)
    year = models.PositiveIntegerField(blank=True, null=True)
    ordering = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['ordering', '-year']

    def __str__(self):
        return self.caption or f"Photo {self.id}"
