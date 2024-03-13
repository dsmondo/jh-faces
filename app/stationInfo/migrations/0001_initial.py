# Generated by Django 5.0.3 on 2024-03-13 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Charging_Station_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Installation_Year', models.TextField(default='')),
                ('Province', models.TextField(default='')),
                ('District', models.TextField(default='')),
                ('Address', models.TextField(default='')),
                ('Charging_Station_Name', models.TextField(default='')),
                ('Facility_Type_Major', models.TextField(default='')),
                ('Facility_Type_Minor', models.TextField(default='')),
                ('Model_Major', models.TextField(default='')),
                ('Model_Minor', models.TextField(default='')),
                ('Operator_Major', models.TextField(default='')),
                ('Operator_Minor', models.TextField(default='')),
                ('Rapid_Charging_Capacity', models.TextField(default='')),
                ('Charger_Type', models.TextField(default='')),
                ('User_Restrictions', models.TextField(default='')),
                ('Charger_ID', models.TextField(default='', unique=True)),
                ('Station_ID', models.TextField(default='', unique=True)),
                ('Latitude', models.TextField(default='')),
                ('Longitude', models.TextField(default='')),
            ],
        ),
    ]
