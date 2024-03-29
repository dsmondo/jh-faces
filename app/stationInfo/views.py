from django.shortcuts import render
from django.db.models import Count
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.conf import settings

from django.contrib.staticfiles import finders

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Charging_Station_Info

import requests
import os
import re
import json

from collections import defaultdict

# .env 파일 로드
from dotenv import load_dotenv

load_dotenv()


def get_ev_charger_info(request, statId):
    # API 요청 URL 구성
    service_key = os.environ.get('DATA_GO_KR_API_KEY')
    url = 'http://apis.data.go.kr/B552584/EvCharger/getChargerInfo'
    params = {
        'serviceKey': service_key,
        'pageNo': '1',
        'numOfRows': '50',
        'dataType': 'JSON'
    }

    if statId != None:
        params['statId'] = statId
    try:
        response = requests.get(url, params=params, timeout=5)
        print(f"Response status_code : {response.status_code}")
        print(f"Response content: {response.content}")
        print(f"Response text: {response.text}")
        data = response.json()  # 응답 데이터를 JSON으로 변환
    except:
        data = None
    # print(f"get_ev_charger_info : {data}")
    return data  # JSON 응답 반환


def get_location_info(request, statId):
    def getLocalData():
        charging_stations = Charging_Station_Info.objects.filter(Station_ID=statId)

        charging_station_info_list = []
        for charging_station in charging_stations:
            if '급속(' in charging_station.Model_Minor:
                output = re.match(re.compile('급속\((\d\d?\d)kW(단?독?|동?시?|멀?티?)\)'),
                                  charging_station.Model_Minor).group(1)
                method = re.match(re.compile('급속\((\d\d?\d)kW(단?독?|동?시?|멀?티?)\)'),
                                  charging_station.Model_Minor).group(2)
            else:
                output = ""
                method = ""

            if charging_station.Charger_Type == 'AC완속':
                chgerType = '02'
            elif charging_station.Charger_Type == 'DC콤보':
                chgerType = '04'
            elif charging_station.Charger_Type == 'DC차데모+AC3상':
                chgerType = '03'
            elif charging_station.Charger_Type == 'DC차데모+AC3상+DC콤보':
                chgerType = '06'

            charging_station_info = {
                'addr': charging_station.Address,
                'bnm': charging_station.Operator_Minor,
                'chgerType': chgerType,
                'chgerId': charging_station.Charger_ID,
                'lat': charging_station.Latitude,
                'lng': charging_station.Longitude,
                "method": output,
                'statNm': charging_station.Charging_Station_Name,
                "output": method,
                'statId': charging_station.Station_ID,
            }
            charging_station_info_list.append(charging_station_info)

        return charging_station_info_list

    try:
        charging_station = Charging_Station_Info.objects.filter(Station_ID=statId).first()
        if charging_station:
            stationLiveInfo = get_ev_charger_info(request, statId)
            logo_exists = {}
            isLive = True

            print(stationLiveInfo)

            if stationLiveInfo == None:
                stationLiveInfo = {'items': {'item': ''}}
                stationLiveInfo['items']['item'] = getLocalData()
                isLive = False

            elif str(stationLiveInfo['items']['item']) == '[]':
                stationLiveInfo['items']['item'] = getLocalData()
                isLive = False

            grouped_items = {}
            for item in stationLiveInfo['items']['item']:
                chger_type = item['chgerType']
                grouped_items.setdefault(chger_type, []).append(item)

                bnm = item['bnm']
                if logo_exists.get(bnm) is None:
                    static_file_path = os.path.join(settings.STATICFILES_DIRS[0], 'business-logo', f'{bnm}.png')
                    static_file_exists = os.path.exists(static_file_path)
                    logo_exists[bnm] = static_file_exists

                for chger_type, items in grouped_items.items():
                    for item in items:
                        bnm = item['bnm']
                        if logo_exists[bnm]:
                            item['hasLogo'] = True
                        else:
                            item['hasLogo'] = False

                stationLiveInfo = grouped_items

            result = {
                'Address': charging_station.Address,
                'Charging_Station_Name': charging_station.Charging_Station_Name,
                'Latitude': charging_station.Latitude,
                'Longitude': charging_station.Longitude,
                'stationLiveInfo': stationLiveInfo,  # Grouped items here
                'logo_exists': logo_exists,
                'isLive': isLive
            }

            return result
        else:
            return None
    except:
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
                                                                   'Model_Major', 'Latitude', 'Longitude').annotate(
            count=Count('Station_ID')).filter(count__gt=1).filter(User_Restrictions='이용가능')

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
                data['ui']['hasLogo'] = stationInfo['logo_exists']
                data['value']['stationInfo'] = stationInfo



        return render(request, "stationInfo/stationInfo.html", context=dict(data=data))
