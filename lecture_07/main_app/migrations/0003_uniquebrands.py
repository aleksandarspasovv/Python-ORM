# Generated by Django 5.0.4 on 2024-07-09 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_migrate_unique_brands'),
    ]

    operations = [
        migrations.CreateModel(
            name='UniqueBrands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=25)),
            ],
        ),
    ]
