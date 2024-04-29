# Generated by Django 5.0.4 on 2024-04-23 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('promotion_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=20)),
                ('discount_percentage', models.DecimalField(decimal_places=2, max_digits=3)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
    ]