# Generated by Django 2.0 on 2018-01-04 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_remove_experiment_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='datarow',
            name='experiment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.Experiment'),
        ),
        migrations.AddField(
            model_name='datarow',
            name='unit',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='experiment',
            name='created',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='experiment',
            name='description',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='experiment',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.Project'),
        ),
        migrations.AddField(
            model_name='value',
            name='datarow',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.Datarow'),
        ),
        migrations.AlterField(
            model_name='datarow',
            name='description',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='value',
            name='value',
            field=models.IntegerField(null=True),
        ),
    ]
