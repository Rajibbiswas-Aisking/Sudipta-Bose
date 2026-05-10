from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0018_alter_serviceitem_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachingitem',
            name='start_year',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='teachingitem',
            name='end_year',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
