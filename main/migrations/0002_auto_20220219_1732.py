# Generated by Django 3.1 on 2022-02-19 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='favorite',
            field=models.BooleanField(default=True),
        ),
    ]
