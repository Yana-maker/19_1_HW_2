# Generated by Django 4.2.4 on 2024-02-21 10:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0019_rename_owner_client_owner_client_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='massage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mailing.text_mailing', verbose_name='тема:'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='time_mailing',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 21, 13, 58, 16, 377330), verbose_name='время рассылки'),
        ),
    ]
