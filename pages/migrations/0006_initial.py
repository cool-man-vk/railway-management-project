# Generated by Django 4.0 on 2021-12-11 13:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pages', '0005_delete_contactdetail_delete_trainmodels'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField(max_length=350)),
            ],
        ),
        migrations.CreateModel(
            name='TrainModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('train_number', models.IntegerField()),
                ('train_name', models.CharField(max_length=50)),
                ('from_date', models.DateField()),
                ('end_date', models.DateField()),
                ('coaches', models.CharField(choices=[('a', '3ac'), ('b', '2ac'), ('c', '1ac')], max_length=10)),
                ('arrival_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('departure_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('source_station', models.CharField(max_length=45)),
                ('dest_station', models.CharField(max_length=50)),
            ],
        ),
    ]
