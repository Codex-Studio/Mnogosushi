# Generated by Django 4.2.5 on 2023-09-26 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='tolal',
            field=models.PositiveBigIntegerField(default=1, verbose_name='Итоговая цена товаров'),
        ),
    ]
