# Generated by Django 5.0.4 on 2024-04-29 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airline', models.CharField(max_length=50)),
                ('flight_date', models.DateField()),
                ('flight_time', models.TimeField()),
                ('departure_city', models.CharField(max_length=20)),
                ('arrival_city', models.CharField(max_length=20)),
                ('duration', models.DecimalField(decimal_places=2, max_digits=4)),
                ('total_seats', models.IntegerField()),
                ('booked_seats', models.IntegerField(default=0)),
                ('fare', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
