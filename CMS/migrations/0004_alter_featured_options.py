# Generated by Django 4.0 on 2021-12-31 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CMS', '0003_remove_featured_collection_featured_collection_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='featured',
            options={'verbose_name': 'Featured Collection', 'verbose_name_plural': 'Featured Collections'},
        ),
    ]
