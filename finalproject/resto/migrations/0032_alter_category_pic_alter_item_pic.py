# Generated by Django 4.2.7 on 2024-04-04 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resto', '0031_alter_order_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='item',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
