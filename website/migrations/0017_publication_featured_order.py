from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('website', '0016_alter_publication_rank'),
    ]
    operations = [
        migrations.AddField(
            model_name='publication',
            name='featured_order',
            field=models.PositiveIntegerField(
                default=0,
                help_text='Display order for featured publications (1 = first). Only applies when featured=True.'
            ),
        ),
    ]
