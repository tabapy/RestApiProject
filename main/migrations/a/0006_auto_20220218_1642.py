# Generated by Django 3.1 on 2022-02-18 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20220218_1509'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='text',
        ),
    ]
