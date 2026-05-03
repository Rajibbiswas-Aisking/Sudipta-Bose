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
        ("conference_paper", "Conference Paper"),
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
    featured = models.BooleanField(default=False)
    journal_or_source = models.CharField(max_length=300, blank=True)
    rank = models.CharField(max_length=20, blank=True, help_text='e.g. FT50, A*, A, B, C (ABDC) or A (APSA)')
    citation_count = models.PositiveIntegerField(null=True, blank=True, help_text='Google Scholar citation count')
    abstract = models.TextField(blank=True)
    abstract_image = models.ImageField(upload_to="abstract_images/", blank=True, null=True)
    link = models.URLField(blank=True)
    volume = models.CharField(max_length=50, blank=True)
    issue = models.CharField(max_length=50, blank=True)
    pages = models.CharField(max_length=50, blank=True, help_text='e.g. 123–138')
    doi = models.CharField(max_length=200, blank=True, help_text='DOI without https://doi.org/')
    publisher = models.CharField(max_length=300, blank=True)
    reference_apa7 = models.TextField(blank=True, help_text='Optional manual APA7 reference override')

    class Meta:
        ordering = ['-year', 'title']

    def __str__(self):
        return f"{self.year} — {self.title}"

    @property
    def apa7_reference(self):
        """Return an APA 7 formatted reference string (uses `reference_apa7` override when present).

        This is a best-effort formatter using available fields. For full control, set
        `reference_apa7` manually in the admin.
        """
        if self.reference_apa7:
            return self.reference_apa7

        parts = []

        if self.authors:
            parts.append(f"{self.authors}")

        if self.year:
            parts.append(f"({self.year}).")

        # Title (italicised in templates) — keep as entered
        if self.title:
            parts.append(f"{self.title}.")

        # Journal / source and publisher
        source_parts = []
        if self.journal_or_source:
            source_parts.append(self.journal_or_source)
        if self.publisher and not self.journal_or_source:
            source_parts.append(self.publisher)

        if source_parts:
            src = ", ".join(source_parts)
            vol_issue = ''
            if self.volume:
                vol_issue += f" {self.volume}"
            if self.issue:
                vol_issue += f"({self.issue})"
            pages = f", {self.pages}" if self.pages else ''
            parts.append(f"{src}{vol_issue}{pages}.")

        # DOI or link
        if self.doi:
            doi_str = self.doi.strip()
            if doi_str.startswith('http'):
                parts.append(doi_str)
            else:
                parts.append(f"https://doi.org/{doi_str}")
        elif self.link:
            parts.append(self.link)

        return ' '.join(p for p in parts if p)


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
    STATUS_CHOICES = [
        ('Current', 'Current'),
        ('Completed', 'Completed'),
    ]

    student_name = models.CharField(max_length=200)
    degree = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='Current')
    role = models.CharField(max_length=100, help_text='Principal supervisor / Co-supervisor')
    topic = models.CharField(max_length=250, blank=True)
    current_position = models.CharField(
        max_length=300, blank=True,
        help_text='Current position or job title of the graduate (for completed supervisions)'
    )
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
