# Generated by Django 4.0 on 2021-12-31 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CMS', '0004_alter_featured_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='featured',
            old_name='sectionDescription',
            new_name='Description',
        ),
    ]
