# Generated by Django 4.2.6 on 2023-10-05 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_cpalink_title_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='cpalink',
            name='slug',
            field=models.SlugField(default=1, max_length=255, unique=True),
            preserve_default=False,
        ),
    ]
