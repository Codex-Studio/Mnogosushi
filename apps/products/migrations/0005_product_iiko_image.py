# Generated by Django 4.2.5 on 2023-11-18 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_sku'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='iiko_image',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Фотография Iiko'),
        ),
    ]
