# Generated by Django 4.2.4 on 2024-01-30 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_product_owner_version'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='owner_version',
        ),
        migrations.RemoveField(
            model_name='version',
            name='owner_version',
        ),
    ]