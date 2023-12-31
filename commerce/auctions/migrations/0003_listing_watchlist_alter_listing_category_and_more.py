# Generated by Django 4.2.7 on 2023-11-09 05:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_listing_comment_bid'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='watchlist',
            field=models.ManyToManyField(blank=True, related_name='watcher', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('NUL', 'Unknown'), ('FAS', 'Fashion'), ('TOY', 'Toys'), ('ELE', 'Electronics'), ('HOM', 'Home'), ('BOK', 'Books'), ('ETC', 'Others')], default='NUL', max_length=3),
        ),
        migrations.AlterField(
            model_name='listing',
            name='image',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
