# Generated by Django 4.2.5 on 2023-09-29 02:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0022_remove_billingproduct_level_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billing',
            name='level',
        ),
        migrations.RemoveField(
            model_name='billing',
            name='lft',
        ),
        migrations.RemoveField(
            model_name='billing',
            name='rght',
        ),
        migrations.RemoveField(
            model_name='billing',
            name='tree_id',
        ),
    ]