# Generated by Django 3.1 on 2022-02-17 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Theme',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='category',
            new_name='theme',
        ),
    ]
