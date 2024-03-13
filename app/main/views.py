from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import pandas as pd

import csv, json

from stationInfo.models import Charging_Station_Info
from django.db.models import Count
from django.core.paginator import Paginator

# Create your views here.
class MainPage(APIView):
    def get(self, request):
        data = {'ui': {}, 'notice_card': {}, 'user': {}, 'value': {}}

        duplicated_stations = Charging_Station_Info.objects.values('Station_ID', 'Charging_Station_Name',
                                                                   'Model_Major').annotate(
            count=Count('Station_ID')).filter(
            count__gt=1).filter(User_Restrictions='이용가능')  # 처음 5개만 가져옵니다.

        # 중복된 Station_ID와 Model_Major를 기준으로 데이터를 추출하고, 각 그룹의 요소 수를 센 후 데이터를 저장합니다.
        result = {}
        for station in duplicated_stations:
            station_id = station['Station_ID']
            charging_station_name = station['Charging_Station_Name']
            model_major = station['Model_Major']
            data_for_station = Charging_Station_Info.objects.filter(Station_ID=station_id,
                                                                    Model_Major=model_major).values()
            count_for_model_major = Charging_Station_Info.objects.filter(Station_ID=station_id,
                                                                         Model_Major=model_major).count()
            result.setdefault(station_id, {}).setdefault('Charging_Station_Name', charging_station_name)
            result.setdefault(station_id, {}).setdefault(model_major, {'count': count_for_model_major, 'data': []}).get(
                'data').extend(data_for_station)

        paginator = Paginator(list(result.values()), 10)  # 한 페이지에 10개씩 표시
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        data['value']['result'] = page_obj

        return render(request, "main/main.html", context=dict(data=data))

