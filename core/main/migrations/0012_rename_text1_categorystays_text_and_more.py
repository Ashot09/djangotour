# Generated by Django 4.0.5 on 2022-06-27 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_categorystays_alter_info2_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categorystays',
            old_name='text1',
            new_name='text',
        ),
        migrations.RemoveField(
            model_name='categorystays',
            name='text2',
        ),
    ]
