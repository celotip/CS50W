# Generated by Django 4.2.7 on 2023-11-09 12:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_listing_current_bidder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(blank=True, choices=[('FAS', 'Fashion'), ('TOY', 'Toys'), ('ELE', 'Electronics'), ('HOM', 'Home'), ('BOK', 'Books'), ('ETC', 'Others'), ('', 'No category listed')], default='', max_length=3),
        ),
        migrations.AlterField(
            model_name='listing',
            name='current_bidder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='current_bid', to=settings.AUTH_USER_MODEL),
        ),
    ]
