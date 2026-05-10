from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0019_add_teachingitem_years'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='abs_rank',
            field=models.CharField(
                blank=True,
                choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('4*', '4*')],
                help_text='ABS Academic Journal Guide rank (1, 2, 3, 4, 4*)',
                max_length=10,
            ),
        ),
        migrations.AddField(
            model_name='publication',
            name='sjr_rank',
            field=models.CharField(
                blank=True,
                choices=[('Q1', 'Q1'), ('Q2', 'Q2'), ('Q3', 'Q3'), ('Q4', 'Q4')],
                help_text='Scimago Journal Rank quartile (Q1–Q4)',
                max_length=5,
            ),
        ),
        migrations.AddField(
            model_name='publication',
            name='publisher_location',
            field=models.CharField(
                blank=True,
                help_text='Publisher location for book chapters, e.g. United Kingdom',
                max_length=200,
            ),
        ),
        migrations.AddField(
            model_name='publication',
            name='editors',
            field=models.CharField(
                blank=True,
                help_text='Book chapter editors, e.g. T. Rana, M. Azim, G. Vesta, & K. Russo',
                max_length=500,
            ),
        ),
        migrations.AddField(
            model_name='publication',
            name='book_title',
            field=models.CharField(
                blank=True,
                help_text='Full book title for book chapters',
                max_length=500,
            ),
        ),
        migrations.AddField(
            model_name='publication',
            name='conference_name',
            field=models.CharField(
                blank=True,
                help_text='Conference paper: name of conference / "presented at"',
                max_length=400,
            ),
        ),
        migrations.AddField(
            model_name='publication',
            name='conference_location',
            field=models.CharField(
                blank=True,
                help_text='Conference paper: city and country of conference',
                max_length=200,
            ),
        ),
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
