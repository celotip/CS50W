# Generated by Django 4.2.7 on 2023-11-26 02:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resto', '0007_alter_user_expiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='expiry',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 26, 2, 31, 47, 66254)),
        ),
    ]
