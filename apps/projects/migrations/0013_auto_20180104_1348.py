# Generated by Django 2.0 on 2018-01-04 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_auto_20180104_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datarow',
            name='experiment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Experiment'),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project'),
        ),
        migrations.AlterField(
            model_name='value',
            name='datarow',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Datarow'),
        ),
    ]