# Generated by Django 4.0 on 2021-12-19 01:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smsUI', '0006_alter_userprofile_joining_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='joining_date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 12, 19, 1, 53, 58, 422180)),
        ),
    ]
