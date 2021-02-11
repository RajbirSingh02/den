# Generated by Django 3.0.8 on 2020-10-07 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('schedule', models.TimeField()),
                ('date', models.DateField()),
                ('message', models.CharField(max_length=100)),
            ],
        ),
    ]