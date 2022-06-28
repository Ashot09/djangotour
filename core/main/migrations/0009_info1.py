# Generated by Django 4.0.5 on 2022-06-26 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_nexttourplace'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media', verbose_name='Info1 image')),
                ('text1', models.CharField(max_length=30, verbose_name='textinfo1')),
                ('text2', models.TextField(verbose_name='textinfo2')),
            ],
        ),
    ]
