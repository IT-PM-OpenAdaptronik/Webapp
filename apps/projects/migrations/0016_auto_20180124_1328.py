# Generated by Django 2.0 on 2018-01-24 13:28

from django.db import migrations

categories = [
    {
        'name': 'Spielzeuge',
        'children': ['Drohne', 'RC-Car']
    },
    {
        'name': 'Fahrzeuge',
        'children': ['PKW', 'LKW', 'Schiff', 'Flugzeug']
    },
    {
        'name': 'Hausgeräte',
        'children': ['Waschmaschine', 'Toaster', 'Küchenmaschine']
    },
    {
        'name': 'Werkzeuge',
        'children': ['Akkuschrauber', 'Bohrmaschine', 'Stichsäge']
    },
    {
        'name': 'Maschinen',
        'children': ['3D-Drucker', 'Drehbank']
    },
    {
        'name': 'IT-Geräte',
        'children': ['Notebook', 'Tablet', 'Digitalkamera']
    },
    {
        'name': 'Gebäude',
        'children': ['Wohnhaus', 'Brücke', 'Tiefgarage']
    },
]

def save(model, name, parent=None):
    try:
        entry = model.objects.get(name=name, parent=parent)
    except model.DoesNotExist:
        entry = model(name=name, parent=parent)
        entry.save()
    return entry

def add_categories(apps, schema_editor):
    Category = apps.get_model("projects", "Category")

    for category in categories:
        parent = save(Category, category['name'])
        for child in category['children']:
            save(Category, child, parent=parent)

def remove_categories(apps, schema_editor):
    Category = apps.get_model("projects", "Category")
    for category in categories:
        try: 
            cat = Category.objects.get(name=category['name'])
            cat.delete()
        except:
            pass

class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0015_auto_20180113_1717'),
    ]

    operations = [
        migrations.RunPython(add_categories, remove_categories)
    ]

