# Generated by Django 4.2.7 on 2023-11-27 12:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resto', '0027_alter_user_expiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='expiry',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 27, 21, 15, 4, 819440)),
        ),
    ]
