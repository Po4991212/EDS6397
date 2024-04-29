# Generated by Django 5.0.4 on 2024-04-26 21:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_alter_booking_reservation_date'),
        ('review', '0002_remove_review_review_id_review_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='booking_id',
        ),
        migrations.AddField(
            model_name='review',
            name='booking',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='booking.booking'),
            preserve_default=False,
        ),
    ]
