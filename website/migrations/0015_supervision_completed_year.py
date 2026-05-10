# Generated migration to add completed_year field to Supervision

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_add_conference_paper_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='supervision',
            name='completed_year',
            field=models.PositiveIntegerField(
                blank=True, null=True,
                help_text='Year the supervision was completed (for completed supervisions)'
            ),
        ),
    ]
