# Generated by Django 5.0.4 on 2024-04-23 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_remove_booking_userprofile_booking_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='status_change_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='total_amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
