from django.db import models


class SiteProfile(models.Model):
    full_name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    institution = models.CharField(max_length=200, blank=True)
    bio = models.TextField()
    research_interests = models.TextField(blank=True)
    skills = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    scholar_url = models.URLField(blank=True)
    orcid_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)

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
        ('journal', 'Journal Article'),
        ('book', 'Book Chapter'),
        ('working', 'Working Paper'),
        ('media', 'Media Article'),
    ]
    title = models.CharField(max_length=300)
    authors = models.CharField(max_length=300)
    year = models.PositiveIntegerField()
    journal_or_source = models.CharField(max_length=255, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='journal')
    link = models.URLField(blank=True)
    abstract = models.TextField(blank=True)
    featured = models.BooleanField(default=False)

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
