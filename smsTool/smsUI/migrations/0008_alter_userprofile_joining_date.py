# Generated by Django 4.0 on 2021-12-19 02:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smsUI', '0007_alter_userprofile_joining_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='joining_date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 12, 19, 2, 18, 50, 188494)),
        ),
    ]