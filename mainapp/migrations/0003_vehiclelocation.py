# Generated by Django 5.0.7 on 2025-03-13 04:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('speed', models.FloatField(blank=True, null=True)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='mainapp.booking')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]
