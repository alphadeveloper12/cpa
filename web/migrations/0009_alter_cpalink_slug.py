# Generated by Django 4.2.6 on 2023-10-05 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_alter_cpalink_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpalink',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]