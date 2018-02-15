# Generated by Django 2.0 on 2018-02-08 09:40

import apps.user.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20180104_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[apps.user.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
    ]
