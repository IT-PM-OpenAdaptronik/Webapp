# Generated by Django 2.0 on 2018-02-08 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0025_auto_20180128_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datarow',
            name='unit',
            field=models.CharField(max_length=10, null=True),
        ),
    ]