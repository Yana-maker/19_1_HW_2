# Generated by Django 4.2.4 on 2024-02-19 20:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0010_alter_mailing_time_mailing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='time_mailing',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 19, 23, 23, 33, 392953), verbose_name='время рассылки'),
        ),
    ]