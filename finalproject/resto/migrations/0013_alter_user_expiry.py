# Generated by Django 4.2.7 on 2023-11-27 00:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resto', '0012_alter_user_expiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='expiry',
            field=models.DateTimeField(default=datetime.time(8, 43, 7, 462457)),
        ),
    ]
