# Generated by Django 5.0.4 on 2024-04-28 19:43

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_alter_booking_reservation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='reservation_date',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(limit_value=datetime.date(2024, 4, 28))]),
        ),
    ]