from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0021_publication_ft50'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='journal_type',
            field=models.CharField(blank=True, choices=[('accounting', 'Accounting Journals'), ('finance', 'Finance Journals'), ('economics', 'Economics Journals'), ('management', 'Management Journals'), ('conference_reviewer', 'Conference reviewer (Adhoc)')], max_length=40),
        ),
    ]
