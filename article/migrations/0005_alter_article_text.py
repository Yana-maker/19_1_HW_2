# Generated by Django 4.2.4 on 2023-09-27 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_alter_article_preview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='text',
            field=models.CharField(max_length=500, verbose_name='содержимое'),
        ),
    ]
