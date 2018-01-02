# Generated by Django 2.0 on 2018-01-02 14:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('categoryID', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('manufacturer', models.CharField(max_length=100)),
                ('typ', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects_category_set', to='projects.Category')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects_subcategory_set', to='projects.Category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('project_imageID', models.IntegerField(primary_key=True, serialize=False)),
                ('projectID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project')),
            ],
        ),
    ]
