# Generated by Django 4.2.6 on 2023-10-05 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_cpalink_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpalink',
            name='slug',
            field=models.SlugField(max_length=255),
        ),
    ]
