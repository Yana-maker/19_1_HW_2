# Generated by Django 4.2.4 on 2023-09-26 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='заголовок')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='article/', verbose_name='фото')),
                ('text', models.CharField(max_length=100, verbose_name='содержимое')),
                ('create_data', models.DateTimeField(verbose_name='дата создания')),
                ('is_published', models.BooleanField(default=True, verbose_name='доступна ли для публикации')),
                ('view_count', models.IntegerField(default=0, verbose_name='просмотры')),
                ('slug', models.CharField(blank=True, max_length=150, null=True, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
                'ordering': ('title',),
            },
        ),
    ]
