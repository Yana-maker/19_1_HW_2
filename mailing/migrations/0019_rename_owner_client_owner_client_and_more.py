# Generated by Django 4.2.4 on 2024-02-21 10:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0018_rename_owner_client_client_owner_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='owner',
            new_name='owner_client',
        ),
        migrations.RenameField(
            model_name='mailing',
            old_name='owner',
            new_name='owner_mailing',
        ),
        migrations.RenameField(
            model_name='text_mailing',
            old_name='owner',
            new_name='owner_text_mailing',
        ),
        migrations.AlterField(
            model_name='mailing',
            name='time_mailing',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 21, 13, 23, 20, 46104), verbose_name='время рассылки'),
        ),
    ]
