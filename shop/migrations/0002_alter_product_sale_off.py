# Generated by Django 4.2 on 2024-07-23 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sale_off',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=20, null=True, verbose_name='Скидка'),
        ),
    ]
