# Generated by Django 4.0.6 on 2022-07-27 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_remove_blog_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='id',
            field=models.UUIDField(primary_key=True, serialize=False),
        ),
    ]
