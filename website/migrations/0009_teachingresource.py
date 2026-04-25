from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_publication_citation_count_publication_rank'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeachingResource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True)),
                ('resource_type', models.CharField(choices=[('reading_list', 'Reading List'), ('lecture_notes', 'Lecture Notes'), ('template', 'Template'), ('external_tool', 'External Tool'), ('assessment_guide', 'Assessment Guide')], max_length=30)),
                ('file', models.FileField(blank=True, null=True, upload_to='teaching_resources/')),
                ('url', models.URLField(blank=True)),
                ('ordering', models.PositiveIntegerField(default=0)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='resources', to='website.teachingitem')),
            ],
            options={
                'ordering': ['ordering', 'resource_type', 'title'],
            },
        ),
    ]
