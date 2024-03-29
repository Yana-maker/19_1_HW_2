# Generated by Django 4.2.4 on 2024-02-25 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=150, verbose_name='название')),
                ('category_description', models.CharField(max_length=150, verbose_name='описание')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
                'ordering': ('category_name',),
            },
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='Почта')),
                ('massage', models.CharField(max_length=150, verbose_name='Краткое описание')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=150, verbose_name='название')),
                ('product_description', models.CharField(max_length=500, verbose_name='описание')),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='фото')),
                ('product_price', models.IntegerField(verbose_name='цена')),
                ('product_created_at', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('product_updated_at', models.DateTimeField(auto_now=True, verbose_name='дата посл изменения')),
                ('is_published', models.BooleanField(default=False, verbose_name='статус публикации')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукты',
                'ordering': ('product_price',),
                'permissions': (('set_product_description', 'редактирование описания продукта'), ('set_product_category', 'редактирование категории продукт'), ('set_product_price', 'цена продукт'), ('set_is_published', 'статус публикации')),
            },
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_version', models.IntegerField(verbose_name='номер')),
                ('name_version', models.CharField(max_length=150, verbose_name='название версии')),
                ('is_current_version', models.BooleanField(default=True, verbose_name='признак версии')),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product', verbose_name='название продукта')),
            ],
            options={
                'verbose_name': 'версия',
                'verbose_name_plural': 'версии',
                'ordering': ('product_name',),
                'permissions': (('set_product_name', 'редактирование продукта'), ('set_number_version', 'редактирование номера версии'), ('set_name_version', 'редактирование названии версии'), ('set_is_current_version', 'редактирование статуса версии')),
            },
        ),
    ]
