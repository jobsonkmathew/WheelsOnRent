# Generated by Django 5.0.7 on 2024-09-21 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0003_rentalpricehistory_competitor_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]