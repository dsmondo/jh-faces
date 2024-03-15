from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from stationInfo.models import Charging_Station_Info
from django.db.models import Count
from django.core.paginator import Paginator

# Create your views here.

