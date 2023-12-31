# Generated by Django 4.2.5 on 2023-10-25 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('billing', '0002_billingmenu_billingmenuproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillingDelivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery', models.CharField(choices=[('Accepted', 'Принят'), ('On way', 'В пути'), ('Delivered', 'Доставлен'), ('Cancel', 'Отменен')], default='Принят', max_length=100, verbose_name='Статус доставки')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('billing', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='billing.billing', verbose_name='Биллинг')),
            ],
            options={
                'verbose_name': 'Доставка',
                'verbose_name_plural': 'Доставки',
            },
        ),
        migrations.CreateModel(
            name='TelegramUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=200, null=True, verbose_name='Имя пользователя')),
                ('user_id', models.CharField(max_length=200, verbose_name='ID пользователя telegram')),
                ('first_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Фамилия')),
                ('user_role', models.CharField(choices=[('User', 'Пользователь'), ('Delivery', 'Курьер'), ('Manager', 'Менеджер')], default='Пользователь', max_length=100, verbose_name='Роль пользователя')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Телеграм пользователь',
                'verbose_name_plural': 'Телеграм пользователи',
            },
        ),
        migrations.CreateModel(
            name='BillingDeliveryHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=200, verbose_name='Сообщение')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время')),
                ('delivery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='delivery_history', to='my_telegram.billingdelivery', verbose_name='Доставка')),
            ],
            options={
                'verbose_name': 'История доставки',
                'verbose_name_plural': 'История доставок',
            },
        ),
        migrations.AddField(
            model_name='billingdelivery',
            name='telegram_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='my_telegram.telegramuser', verbose_name='Пользователь'),
        ),
    ]
