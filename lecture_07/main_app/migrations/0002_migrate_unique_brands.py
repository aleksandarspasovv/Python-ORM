# Generated by Django 5.0.4 on 2024-07-09 18:46

from django.db import migrations


def create_unique_brands(apps, schema_editor):
    shoe = apps.get_model('main_app', 'Shoe')
    unique_brands = apps.get_model('main_app', 'UniqueBrand')

    db_alias = schema_editor.connection.alias
    unique_brand_names = shoe.objects.values_list('brand', flat=True).distinct()

    for brand_name in unique_brand_names:
        unique_brands.objects.using(db_alias).create(brand_name=brand_name)



class Migration(migrations.Migration):
    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_unique_brands)
    ]
