# Generated by Django 4.0.5 on 2022-06-26 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_offergoods'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offergoods',
            name='price',
            field=models.IntegerField(verbose_name='Goods price'),
        ),
    ]
