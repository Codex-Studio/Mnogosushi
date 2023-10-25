# Generated by Django 4.2.5 on 2023-10-25 01:01

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_image'),
        ('billing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillingMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.PositiveIntegerField(verbose_name='Итоговая цена товаров')),
                ('payment_method', models.CharField(default='Наличные', max_length=100, verbose_name='Способ оплаты')),
                ('payment_code', models.CharField(max_length=20, unique=True, verbose_name='Код оплаты биллинга')),
                ('status', models.BooleanField(default=False, verbose_name='Статус заказа')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания биллинга')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='billing.billingmenu')),
            ],
            options={
                'verbose_name': 'Биллинг (Menu)',
                'verbose_name_plural': 'Биллинги (Menu)',
            },
        ),
        migrations.CreateModel(
            name='BillingMenuProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(verbose_name='Количество товаров')),
                ('price', models.PositiveBigIntegerField(default=0, verbose_name='Итоговая цена')),
                ('status', models.BooleanField(default=False, verbose_name='Статус')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('billing', mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='billing_menu_products', to='billing.billingmenu')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Продукт биллинга',
                'verbose_name_plural': 'Продукты биллингов',
            },
        ),
    ]
