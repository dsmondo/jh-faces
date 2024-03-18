from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from django.db.models import Count
from django.core.paginator import Paginator

# Create your views here.

from stationInfo.models import Charging_Station_Info

import requests
from django.http import JsonResponse

def get_ev_charger_info(request, statId):
    # API 요청 URL 구성
    service_key = os.environ.get('DATA_GO_KR_API_KEY')
    url = 'http://apis.data.go.kr/B552584/EvCharger/getChargerInfo'
    params = {
        'serviceKey': service_key,
        'pageNo': '1',
        'numOfRows': '10',
        'dataType': 'JSON'
    }

    if statId != None:
        params['statId'] = statId

    response = requests.get(url, params=params)
    data = response.json()  # 응답 데이터를 JSON으로 변환

    return data  # JSON 응답 반환

def get_location_info(request, statId):
    try:
        charging_station = Charging_Station_Info.objects.filter(Station_ID=statId).first()
        if charging_station:
            result = {
                'Address': charging_station.Address,
                'Charging_Station_Name': charging_station.Charging_Station_Name,
                'Latitude': charging_station.Latitude,
                'Longitude': charging_station.Longitude,
                'stationLiveInfo': get_ev_charger_info(request, statId)
            }
            return result
        else:
            return None
    except Charging_Station_Info.DoesNotExist:
        return None


class TestJson(APIView):
    def get(self, request):
        data = {'ui': {}, 'notice_card': {}, 'user': {}, 'value': {}}

        statId = request.GET.get('statId')
        result = get_ev_charger_info(request, statId)

        data['value']['result'] = result

        return render(request, "test/json.html", context=dict(data=data))

class MainPage(APIView):
    def get(self, request):
        data = {'ui': {}, 'notice_card': {}, 'user': {}, 'value': {}}

        duplicated_stations = Charging_Station_Info.objects.values('Station_ID', 'Charging_Station_Name',
                                                                   'Model_Major', 'Latitude', 'Longitude').annotate(count=Count('Station_ID')).filter(count__gt=1).filter(User_Restrictions='이용가능')

        # 중복된 Station_ID와 Model_Major를 기준으로 데이터를 추출하고, 각 그룹의 요소 수를 센 후 데이터를 저장합니다.
        result = {}
        for station in duplicated_stations:
            station_id = station['Station_ID']
            charging_station_name = station['Charging_Station_Name']
            model_major = station['Model_Major']
            latitude = station['Latitude']  # Added Latitude
            longitude = station['Longitude']  # Added Longitude
            data_for_station = Charging_Station_Info.objects.filter(Station_ID=station_id,
                                                                    Model_Major=model_major).values()
            count_for_model_major = Charging_Station_Info.objects.filter(Station_ID=station_id,
                                                                         Model_Major=model_major).count()
            result.setdefault(station_id, {}).setdefault('Charging_Station_Name', charging_station_name)
            result.setdefault(station_id, {}).setdefault(model_major, {'count': count_for_model_major, 'data': []}).get(
                'data').extend(data_for_station)

            result[station_id]['Station_ID'] = station_id
            result[station_id]['Latitude'] = latitude  # Added Latitude
            result[station_id]['Longitude'] = longitude  # Added Longitude

        paginator = Paginator(list(result.values()), 10)  # 한 페이지에 10개씩 표시
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        data['value']['result'] = page_obj
        if request.GET.get('stationID'):
            stationID = request.GET.get('stationID')
            stationInfo = get_location_info(request, stationID)
            if stationInfo != None:
                data['ui']['isDetail'] = True
                data['value']['stationInfo'] = stationInfo

        return render(request, "stationInfo/main.html", context=dict(data=data))

