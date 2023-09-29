# Generated by Django 4.2.5 on 2023-09-29 02:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0018_billingproduct_parent'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SaleSummary',
        ),
        migrations.CreateModel(
            name='SaleSummary',
            fields=[
                ('billing_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='billing.billing')),
            ],
            options={
                'verbose_name': 'Отчет продажа товар',
                'verbose_name_plural': 'Отчеты продажи товаров',
            },
            bases=('billing.billing',),
        ),
    ]
