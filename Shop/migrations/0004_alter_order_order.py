# Generated by Django 4.0 on 2022-01-12 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0003_alter_order_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order',
            field=models.CharField(max_length=5000),
        ),
    ]