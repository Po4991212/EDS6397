# Generated by Django 5.0.4 on 2024-04-23 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=5),
            preserve_default=False,
        ),
    ]
