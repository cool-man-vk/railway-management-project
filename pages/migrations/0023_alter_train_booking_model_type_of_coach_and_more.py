# Generated by Django 4.0 on 2021-12-14 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0022_alter_train_booking_model_type_of_coach'),
    ]

    operations = [
        migrations.AlterField(
            model_name='train_booking_model',
            name='type_of_coach',
            field=models.BooleanField(blank=True, choices=[('a', '3ac'), ('b', '2ac'), ('c', '1ac')], default='a'),
        ),
        migrations.AlterField(
            model_name='trainmodels',
            name='coaches',
            field=models.BooleanField(blank=True, choices=[('a', '3ac'), ('b', '2ac'), ('c', '1ac')], default='a'),
        ),
    ]
