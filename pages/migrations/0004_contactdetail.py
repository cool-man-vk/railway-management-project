# Generated by Django 4.0 on 2021-12-11 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_initial'),
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
    ]
