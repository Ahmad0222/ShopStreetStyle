# Generated by Django 4.0 on 2021-12-31 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0003_product_best_selling_product_featured_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-id'], 'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
    ]
