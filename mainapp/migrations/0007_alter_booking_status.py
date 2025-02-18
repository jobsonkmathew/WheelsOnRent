# Generated by Django 5.0.7 on 2025-01-29 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_user_auth_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('picked_up', 'Picked Up'), ('returned', 'Returned'), ('cancelled', 'Cancelled'), ('completed', 'Completed')], default='pending', max_length=20),
        ),
    ]
