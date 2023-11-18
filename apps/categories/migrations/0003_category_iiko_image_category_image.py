# Generated by Django 4.2.5 on 2023-11-18 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_category_external_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='iiko_image',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Фотография Iiko'),
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='category_image/', verbose_name='Фотография категории'),
        ),
    ]
