# Generated by Django 4.0 on 2021-12-13 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('pages', '0017_alter_train_booking_model_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='train_booking_model',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trainbookingmodel', to='auth.user'),
        ),
    ]
