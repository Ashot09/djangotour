# Generated by Django 4.0.5 on 2022-06-27 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_info2_alter_info1_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryStays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text1', models.TextField(verbose_name='rent')),
                ('text2', models.TextField(verbose_name='sell')),
            ],
            options={
                'verbose_name': 'CategoryStays',
                'verbose_name_plural': 'CategoryStayss',
            },
        ),
        migrations.AlterModelOptions(
            name='info2',
            options={'verbose_name': 'Info2', 'verbose_name_plural': 'Info2'},
        ),
    ]
