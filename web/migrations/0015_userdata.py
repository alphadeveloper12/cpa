# Generated by Django 4.2.6 on 2023-10-05 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0014_contactmessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('country', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
            ],
        ),
    ]