# Generated by Django 4.0 on 2021-12-13 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_personsdetailsmodel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='train_booking_model',
            name='date_of_birth',
            field=models.DateField(),
        ),
    ]
