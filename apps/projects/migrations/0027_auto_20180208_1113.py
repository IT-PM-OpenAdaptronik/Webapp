# Generated by Django 2.0 on 2018-02-08 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0026_auto_20180202_0947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='measured',
        ),
        migrations.AddField(
            model_name='experiment',
            name='measured',
            field=models.DateTimeField(null=True),
        ),
    ]
