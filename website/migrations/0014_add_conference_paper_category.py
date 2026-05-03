# Generated migration to add conference_paper category

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_publication_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='category',
            field=models.CharField(
                choices=[
                    ('published_paper', 'Published Paper'),
                    ('conference_paper', 'Conference Paper'),
                    ('media_article', 'Media Article'),
                    ('book_chapter', 'Book Chapter'),
                    ('journal_reviewer', 'Journal Reviewer'),
                    ('journal_published', 'Journal Published'),
                    ('working_paper', 'Working Paper'),
                ],
                max_length=30,
            ),
        ),
    ]
