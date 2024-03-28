# Generated by Django 5.0.3 on 2024-03-28 00:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("marketTools", "0003_remove_resultgeo_area_alter_resultgeo_unnamed_0"),
    ]

    operations = [
        migrations.CreateModel(
            name="RecommandGEO",
            fields=[
                ("unnamed_0", models.IntegerField(blank=True, null=True)),
                ("fid", models.IntegerField(blank=True, null=True)),
                (
                    "gid",
                    models.CharField(max_length=255, primary_key=True, serialize=False),
                ),
                ("emd_cd", models.IntegerField()),
                ("emd_nm_k", models.CharField(max_length=255)),
                ("charging_station_accessibility", models.FloatField()),
                ("gas_station_count", models.IntegerField()),
                ("charging_station_count", models.IntegerField()),
                ("performance_facility_accessibility", models.FloatField()),
                ("public_price", models.FloatField()),
                ("library_accessibility", models.FloatField()),
                ("hospital_accessibility", models.FloatField()),
                ("health_center_accessibility", models.FloatField()),
                ("community_park_accessibility", models.FloatField()),
                ("fire_station_accessibility", models.FloatField()),
                ("population", models.IntegerField()),
                ("theme_park_accessibility", models.FloatField()),
                ("parking_lot_accessibility", models.FloatField()),
                ("sports_facility_accessibility", models.FloatField()),
                ("elementary_school_accessibility", models.FloatField()),
                ("fast_charging", models.IntegerField()),
                ("agricultural_area", models.IntegerField()),
                ("altitude", models.IntegerField()),
                ("river", models.IntegerField()),
                ("center_coordinates", models.CharField(max_length=255)),
                ("y_pred_rf", models.IntegerField()),
                ("y_pred_lgb", models.IntegerField()),
                ("y_pred_xgb", models.IntegerField()),
                ("y_pred_voting", models.IntegerField()),
                ("cluster_id", models.IntegerField()),
                ("cluster_size", models.IntegerField()),
                ("coordinates", models.JSONField()),
                ("type", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "detailed_category",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("district_code", models.IntegerField(blank=True, null=True)),
                ("road_name_code", models.IntegerField(blank=True, null=True)),
                (
                    "road_address",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "institution_name",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("position_x", models.FloatField(blank=True, null=True)),
                ("position_y", models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
