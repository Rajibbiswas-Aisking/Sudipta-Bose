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
    featured_order = models.PositiveIntegerField(
        default=0,
        help_text='Display order for featured publications (1 = first). Only applies when featured=True.'
    )
    ft50 = models.BooleanField(default=False, help_text='Tick this for FT50 journal publications.')
    journal_or_source = models.CharField(max_length=300, blank=True)
    JOURNAL_TYPE_CHOICES = [
        ('accounting', 'Accounting Journals'),
        ('finance', 'Finance Journals'),
        ('economics', 'Economics Journals'),
        ('management', 'Management Journals'),
        ('conference_reviewer', 'Conference reviewer (Adhoc)'),
    ]
    journal_type = models.CharField(max_length=40, choices=JOURNAL_TYPE_CHOICES, blank=True)
    rank = models.CharField(max_length=20, blank=True, help_text='e.g. A*, A, B, C (ABDC) or A (APSA)')
    abs_rank = models.CharField(
        max_length=10,
        blank=True,
        choices=[
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('4*', '4*'),
        ],
        help_text='ABS Academic Journal Guide rank (1, 2, 3, 4, 4*)'
    )
    sjr_rank = models.CharField(
        max_length=5,
        blank=True,
        choices=[
            ('Q1', 'Q1'),
            ('Q2', 'Q2'),
            ('Q3', 'Q3'),
            ('Q4', 'Q4'),
        ],
        help_text='Scimago Journal Rank quartile (Q1–Q4)'
    )
    citation_count = models.PositiveIntegerField(null=True, blank=True, help_text='Google Scholar citation count')
    abstract = models.TextField(blank=True)
    abstract_image = models.ImageField(upload_to="abstract_images/", blank=True, null=True)
    link = models.URLField(blank=True)
    volume = models.CharField(max_length=50, blank=True)
    issue = models.CharField(max_length=50, blank=True)
    pages = models.CharField(max_length=50, blank=True, help_text='e.g. 123–138')
    doi = models.CharField(max_length=200, blank=True, help_text='DOI without https://doi.org/')
    publisher = models.CharField(max_length=300, blank=True)
    publisher_location = models.CharField(
        max_length=200,
        blank=True,
        help_text='Publisher location for book chapters, e.g. United Kingdom'
    )
    editors = models.CharField(
        max_length=500,
        blank=True,
        help_text='Book chapter editors, e.g. T. Rana, M. Azim, G. Vesta, & K. Russo'
    )
    book_title = models.CharField(
        max_length=500,
        blank=True,
        help_text='Full book title for book chapters'
    )
    conference_name = models.CharField(
        max_length=400,
        blank=True,
        help_text='Conference paper: name of conference / "presented at"'
    )
    conference_location = models.CharField(
        max_length=200,
        blank=True,
        help_text='Conference paper: city and country of conference'
    )
    reference_apa7 = models.TextField(blank=True, help_text='Optional manual APA7 reference override')

    class Meta:
        ordering = ['-year', 'title']

    def __str__(self):
        return f"{self.year} — {self.title}"

    @property
    def apa7_reference(self):
        """
        Return an APA 7 formatted reference string.
        Uses `reference_apa7` override when present.
        Handles journal articles, book chapters, conference papers, and working papers.
        """
        if self.reference_apa7:
            return self.reference_apa7

        # ── Book Chapter ────────────────────────────────────────────────────────
        if self.category == 'book_chapter':
            parts = []
            if self.authors:
                parts.append(self.authors)
            if self.year:
                parts.append(f"({self.year}).")
            if self.title:
                parts.append(f"{self.title}.")

            # In Editors (Eds.), Book Title (pp. X–Y).
            pages_str = f" (pp. {self.pages})" if self.pages else ""
            if self.editors and self.book_title:
                parts.append(f"In {self.editors} (Eds.), {self.book_title}{pages_str}.")
            elif self.editors:
                parts.append(f"In {self.editors} (Eds.).")
            elif self.book_title:
                parts.append(f"In {self.book_title}{pages_str}.")

            # Publisher location: Publisher.
            if self.publisher_location and self.publisher:
                parts.append(f"{self.publisher_location}: {self.publisher}.")
            elif self.publisher:
                parts.append(f"{self.publisher}.")
            elif self.publisher_location:
                parts.append(f"{self.publisher_location}.")

            # DOI
            if self.doi:
                doi_str = self.doi.strip()
                parts.append(doi_str if doi_str.startswith('http') else f"https://doi.org/{doi_str}")
            elif self.link:
                parts.append(self.link)

            # APSA rank suffix — for book chapters, the `rank` field holds the APSA rank
            if self.rank:
                parts.append(f"(APSA RANK: {self.rank}).")

            return ' '.join(p for p in parts if p)

        # ── Conference Paper ─────────────────────────────────────────────────────
        if self.category == 'conference_paper':
            parts = []
            if self.authors:
                parts.append(self.authors)
            if self.year:
                parts.append(f"({self.year}).")
            if self.title:
                parts.append(f"{self.title}.")

            conf_parts = []
            if self.conference_name:
                conf_parts.append(self.conference_name)
            if self.conference_location:
                conf_parts.append(self.conference_location)
            if conf_parts:
                parts.append(f"Paper presented at {', '.join(conf_parts)}.")

            if self.doi:
                doi_str = self.doi.strip()
                parts.append(doi_str if doi_str.startswith('http') else f"https://doi.org/{doi_str}")
            elif self.link:
                parts.append(self.link)

            return ' '.join(p for p in parts if p)

        # ── Journal / Working Paper / Media / Default ────────────────────────────
        parts = []
        if self.authors:
            parts.append(self.authors)
        if self.year:
            parts.append(f"({self.year}).")
        if self.title:
            parts.append(f"{self.title}.")

        source_parts = []
        if self.journal_or_source:
            source_parts.append(self.journal_or_source)
        elif self.publisher:
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

        if self.doi:
            doi_str = self.doi.strip()
            parts.append(doi_str if doi_str.startswith('http') else f"https://doi.org/{doi_str}")
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
    start_year = models.CharField(max_length=20, blank=True)
    end_year = models.CharField(max_length=20, blank=True)
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
    completed_year = models.PositiveIntegerField(
        blank=True, null=True,
        help_text='Year the supervision was completed (for completed supervisions)'
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
        ordering = ['ordering']

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
