# Generated by Django 5.0.7 on 2024-08-11 21:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0005_vehicle_image_alter_image_vehicle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicles', to='vendor.vendor'),
        ),
    ]