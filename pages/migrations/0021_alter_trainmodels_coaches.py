# Generated by Django 4.0 on 2021-12-14 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0020_alter_trainmodels_coaches'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainmodels',
            name='coaches',
            field=models.BooleanField(choices=[('a', '3ac'), ('b', '2ac'), ('c', '1ac')], default='a'),
        ),
    ]
