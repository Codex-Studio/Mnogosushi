# Generated by Django 4.2.5 on 2023-09-26 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=200, null=True, verbose_name='Имя пользователя')),
                ('user_id', models.CharField(max_length=200, verbose_name='ID пользователя telegram')),
                ('first_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Фамилия')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Телеграм пользователь',
                'verbose_name_plural': 'Телеграм пользователи',
            },
        ),
    ]
