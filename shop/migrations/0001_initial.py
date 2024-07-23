# Generated by Django 4.2 on 2024-07-23 07:37

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
                ('category_name', models.CharField(max_length=255, verbose_name='Категория')),
                ('slug', models.CharField(max_length=255, verbose_name='Слаг для категрий')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255, verbose_name='Компания')),
                ('slug', models.CharField(max_length=255, verbose_name='Слаг для компаний')),
            ],
            options={
                'verbose_name': 'Комания',
                'verbose_name_plural': 'Компании',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=3, max_digits=20, verbose_name='Цена')),
                ('model_name', models.CharField(max_length=255, verbose_name='Имя товара')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image1', models.ImageField(upload_to='images', verbose_name='Главная картинка')),
                ('image2', models.ImageField(blank=True, upload_to='images', verbose_name='Вторая картинка')),
                ('image3', models.ImageField(blank=True, upload_to='images', verbose_name='Третья картинка')),
                ('count', models.IntegerField(verbose_name='Количество товара')),
                ('characteristcs', models.TextField(verbose_name='Характеристики товара')),
                ('sale_off', models.DecimalField(blank=True, decimal_places=3, max_digits=20, verbose_name='Скидка')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('likes', models.BooleanField(blank=True, verbose_name='Избранные')),
                ('category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category', verbose_name='Название категорий')),
                ('company_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.company', verbose_name='Название Компаний')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]
