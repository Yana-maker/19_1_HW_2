# Generated by Django 4.2.4 on 2023-09-05 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_category_options_alter_product_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='created_at',
            field=models.CharField(default=0, max_length=150, verbose_name='создано кем'),
        ),
    ]
