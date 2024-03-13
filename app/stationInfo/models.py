from django.db import models
from datetime import datetime

class Charging_Station_Info(models.Model):
    Installation_Year = models.TextField(default='')
    Province = models.TextField(default='')
    District = models.TextField(default='')
    Address = models.TextField(default='')
    Charging_Station_Name = models.TextField(default='')
    Facility_Type_Major = models.TextField(default='')
    Facility_Type_Minor = models.TextField(default='')
    Model_Major = models.TextField(default='')
    Model_Minor = models.TextField(default='')
    Operator_Major = models.TextField(default='')
    Operator_Minor = models.TextField(default='')
    Rapid_Charging_Capacity = models.TextField(default='')
    Charger_Type = models.TextField(default='')
    User_Restrictions = models.TextField(default='')
    Charger_ID = models.TextField(default='',)
    Station_ID = models.TextField(default='')
    Latitude = models.TextField(default='')
    Longitude = models.TextField(default='')