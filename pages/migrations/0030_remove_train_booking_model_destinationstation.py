# Generated by Django 4.0 on 2021-12-16 03:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0029_remove_train_booking_model_arrivaltime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='train_booking_model',
            name='destinationStation',
        ),
    ]
