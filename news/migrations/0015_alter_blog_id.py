# Generated by Django 4.0.6 on 2022-07-27 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0014_alter_blog_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
