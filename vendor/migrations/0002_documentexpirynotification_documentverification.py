# Generated by Django 5.0.7 on 2025-04-06 19:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentExpiryNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_type', models.CharField(choices=[('registration', 'Vehicle Registration'), ('insurance', 'Insurance'), ('puc', 'PUC Certificate'), ('fitness', 'Fitness Certificate')], max_length=20)),
                ('expiry_date', models.DateField()),
                ('notification_date', models.DateField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('sent', 'Sent'), ('read', 'Read')], default='pending', max_length=10)),
                ('sent_at', models.DateTimeField(blank=True, null=True)),
                ('read_at', models.DateTimeField(blank=True, null=True)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expiry_notifications', to='vendor.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='DocumentVerification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('verified', 'Verified'), ('failed', 'Failed')], default='pending', max_length=20)),
                ('verified_at', models.DateTimeField(blank=True, null=True)),
                ('verification_notes', models.TextField(blank=True, null=True)),
                ('extracted_rc_number', models.CharField(blank=True, max_length=50, null=True)),
                ('extracted_insurance_number', models.CharField(blank=True, max_length=50, null=True)),
                ('extracted_insurance_expiry', models.DateField(blank=True, null=True)),
                ('extracted_puc_expiry', models.DateField(blank=True, null=True)),
                ('rc_verified', models.BooleanField(default=False)),
                ('insurance_verified', models.BooleanField(default=False)),
                ('puc_verified', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('vehicle_document', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='verification', to='vendor.vehicledocument')),
            ],
        ),
    ]
