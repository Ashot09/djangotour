# Generated by Django 4.0.5 on 2022-06-27 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_rename_text1_categorystays_text_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorystays',
            options={'verbose_name': 'CategoryStays', 'verbose_name_plural': 'CategoryStays'},
        ),
        migrations.RenameField(
            model_name='categorystays',
            old_name='text',
            new_name='name',
        ),
    ]
