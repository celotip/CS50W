# Generated by Django 4.2.7 on 2023-11-27 12:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resto', '0022_alter_user_expiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='expiry',
            field=models.TimeField(default=datetime.time(20, 56, 44, 477577)),
        ),
    ]
