# Generated by Django 4.1.3 on 2024-03-07 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PatientModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('healthcard_number', models.CharField(max_length=100)),
                ('appointment_timings', models.DateTimeField()),
                ('priority', models.CharField(max_length=100)),
                ('symptoms', models.TextField()),
                ('diagnoses', models.TextField()),
            ],
        ),
    ]
