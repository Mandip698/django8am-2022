# Generated by Django 4.0.6 on 2022-07-19 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='setting',
            old_name='favicom',
            new_name='favicon',
        ),
    ]
