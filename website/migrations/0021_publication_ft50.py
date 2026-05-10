from django.db import migrations, models


def backfill_ft50(apps, schema_editor):
    Publication = apps.get_model('website', 'Publication')
    Publication.objects.filter(rank='FT50').update(ft50=True, rank='')


def reverse_backfill_ft50(apps, schema_editor):
    Publication = apps.get_model('website', 'Publication')
    Publication.objects.filter(ft50=True, rank='').update(rank='FT50', ft50=False)


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0020_publication_ranks_conference'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='ft50',
            field=models.BooleanField(default=False, help_text='Tick this for FT50 journal publications.'),
        ),
        migrations.RunPython(backfill_ft50, reverse_backfill_ft50),
    ]