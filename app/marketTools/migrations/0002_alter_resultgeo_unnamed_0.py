# Generated by Django 5.0.3 on 2024-03-27 01:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("marketTools", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="resultgeo",
            name="unnamed_0",
            field=models.IntegerField(default=0),
        ),
    ]
