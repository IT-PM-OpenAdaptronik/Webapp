# Generated by Django 2.0 on 2017-12-29 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_visibility',
            field=models.BooleanField(default=True),
        ),
    ]
