# Generated by Django 4.2.7 on 2023-11-27 00:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resto', '0010_alter_user_expiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='expiry',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 27, 8, 33, 27, 144026)),
        ),
    ]
