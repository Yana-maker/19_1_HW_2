# Generated by Django 4.2.4 on 2024-02-21 09:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0014_remove_text_mailing_client_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='time_mailing',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 21, 12, 46, 50, 575932), verbose_name='время рассылки'),
        ),
    ]