# Generated by Django 4.2.7 on 2023-11-27 00:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resto', '0014_alter_user_expiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='expiry',
            field=models.TimeField(default=datetime.time(8, 53, 45, 15901)),
        ),
    ]
