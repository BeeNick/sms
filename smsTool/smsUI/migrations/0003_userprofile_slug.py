# Generated by Django 4.0 on 2021-12-18 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smsUI', '0002_alter_personalskills_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='slug',
            field=models.SlugField(default='user'),
        ),
    ]