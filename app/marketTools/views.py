from django.shortcuts import render
from django.db.models import Q
from django.contrib.staticfiles import finders

from rest_framework.views import APIView


from .models import ResultGEO
from .models import RecommandGEO
from .models import RecommandGSGEO
from .models import existInstalledGEO
from .models import existInstalledGridGEO

import os
import json

# .env 파일 로드
from dotenv import load_dotenv

load_dotenv()

def loadDATA():
    from .geoJSONtoDB import migrate_existInstalledGEO
    migrate_existInstalledGEO(finders.find('급속이필요한곳.geojson'))


class MainPage(APIView):
    def get(self, request):
        data = {'ui': {}, 'notice_card': {}, 'user': {}, 'value': {}}

        downloadURL = os.environ.get('FINAL_DOCS_DOWNLOAD_URL')
        data['value']['downloadURL'] = downloadURL

        level = request.GET.get('level')
        lat = request.GET.get('lat')
        lng = request.GET.get('lng')

        if level != None and lat != None and lng != None:
            data['ui']['mapInfo'] = {"level": level, "lat": lat, "lng": lng}

        minPrice = request.GET.get('minPrice')
        maxPrice = request.GET.get('maxPrice')
        gfid = request.GET.get('gfid')
        if gfid != None:
            if not gfid.isdigit():
                gfid = None
                data['ui']['searchData'] = 'None'

        # ResultGEO
        if gfid == None:  # 검색값이 없는 경우
            resultGEO1_param = request.GET.get('ResultGEO1')
            resultGEO2_param = request.GET.get('ResultGEO2')
            resultGEO3_param = request.GET.get('ResultGEO3')

            resultGEO_filter = []
            if resultGEO1_param == 'true':
                resultGEO_filter.append(1)
            if resultGEO2_param == 'true':
                resultGEO_filter.append(2)
            if resultGEO3_param == 'true':
                resultGEO_filter.append(3)

            resultGEO_object = ResultGEO.objects.filter(y_pred_lgb__in=resultGEO_filter)

            if minPrice != None:
                if minPrice != 'null':
                    resultGEO_object = resultGEO_object.filter(public_price__gt=int(minPrice))
            if maxPrice != None:
                if maxPrice != 'null':
                    resultGEO_object = resultGEO_object.filter(public_price__lt=int(maxPrice))
        else:  # 검색값이 있는 경우
            resultGEO_object = ResultGEO.objects.filter(Q(gid=gfid) | Q(fid=gfid))
            if resultGEO_object.exists():
                data['ui']['searchData'] = 'resultGEO'

        resultGEO_output = {"features": []}
        for i in resultGEO_object:
            name = i.fid  # GID
            gid = i.gid  # GID
            fid = i.fid  # GID
            y_pred_lgb = i.y_pred_lgb  # 급완속 여부
            public_price = i.public_price  # 공시지가
            population = i.population  # 인구
            altitude = i.altitude  # 고도
            emd_nm_k = i.emd_nm_k  # 법정동

            geometry = i.coordinates
            if y_pred_lgb == 1:
                color = '#F0766F'
            if y_pred_lgb == 2:
                color = '#4277F1'
            if y_pred_lgb == 3:
                color = '#BE83B9'
            resultGEO_output['features'].append(
                {"properties": {"name": name, "gid": gid, "fid": fid, "y_pred_lgb": y_pred_lgb,
                                "public_price": public_price, "population": population,
                                "altitude": altitude, "emd_nm_k": emd_nm_k, "color": color}, "geometry": geometry})

        # RecommandGEO
        if gfid == None:  # 검색값이 없는 경우

            recommandGEO1_param = request.GET.get('RecommandGEO1')  # 급속
            recommandGEO2_param = request.GET.get('RecommandGEO2')  # 완속
            recommandGEO3_param = request.GET.get('RecommandGEO3')  # 급/완속

            recommandGEO_filter = []
            if recommandGEO1_param == 'true':
                recommandGEO_filter.append(1)
            if recommandGEO2_param == 'true':
                recommandGEO_filter.append(2)
            if recommandGEO3_param == 'true':
                recommandGEO_filter.append(3)

            recommandGEO_object = RecommandGEO.objects.filter(y_pred_lgb__in=recommandGEO_filter)

            if minPrice != None:
                if minPrice != 'null':
                    recommandGEO_object = recommandGEO_object.filter(public_price__gt=int(minPrice))
            if maxPrice != None:
                if maxPrice != 'null':
                    recommandGEO_object = recommandGEO_object.filter(public_price__lt=int(maxPrice))

        else:  # 검색값이 있는 경우
            recommandGEO_object = RecommandGEO.objects.filter(Q(gid=gfid) | Q(fid=gfid))
            if recommandGEO_object.exists():
                data['ui']['searchData'] = 'recommandGEO'

        recommandGEO_output = {"features": []}
        for i in recommandGEO_object:
            name = i.institution_name  # GID
            gid = i.gid  # GID
            fid = i.fid  # GID
            y_pred_lgb = i.y_pred_lgb  # 급완속 여부
            public_price = i.public_price  # 공시지가
            population = i.population  # 인구
            altitude = i.altitude  # 고도
            emd_nm_k = i.emd_nm_k  # 법정동

            geometry = i.coordinates
            if y_pred_lgb == 1:
                color = '#1D3557'
            if y_pred_lgb == 2:
                color = '#457B9D'
            if y_pred_lgb == 3:
                color = '#750D37'

            recommandGEO_output['features'].append(
                {"properties": {"name": name, "gid": gid, "fid": fid, "y_pred_lgb": y_pred_lgb,
                                "public_price": public_price, "population": population,
                                "altitude": altitude, "emd_nm_k": emd_nm_k, "color": color}, "geometry": geometry})

        # RecommandGSGEO
        if gfid == None:  # 검색값이 없는 경우
            recommandGSGEO_param = request.GET.get('RecommandGSGEO')  # 주유소

            if recommandGSGEO_param == 'true':
                recommandGSGEO_object = RecommandGSGEO.objects.all()

                if minPrice != None:
                    if minPrice != 'null':
                        recommandGSGEO_object = recommandGSGEO_object.filter(public_price__gt=int(minPrice))
                if maxPrice != None:
                    if maxPrice != 'null':
                        recommandGSGEO_object = recommandGSGEO_object.filter(public_price__lt=int(maxPrice))


        else:  # 검색값이 있는 경우
            recommandGSGEO_object = RecommandGSGEO.objects.filter(Q(gid=gfid) | Q(fid=gfid))
            if recommandGSGEO_object.exists():
                data['ui']['searchData'] = 'recommandGSGEO'

        recommandGSGEO_output = {"features": []}
        try:
            for i in recommandGSGEO_object:
                name = i.gas_station_name  # GID
                gid = i.gid  # GID
                fid = i.fid  # GID
                y_pred_lgb = i.y_pred_lgb  # 급완속 여부
                public_price = i.public_price  # 공시지가
                population = i.population  # 인구
                altitude = i.altitude  # 고도
                emd_nm_k = i.emd_nm_k  # 법정동

                geometry = {'type': 'MultiPoint', 'coordinates': [[i.longitude, i.latitude]]}
                color = '#B87D4B'

                recommandGSGEO_output['features'].append(
                    {"properties": {"name": name, "gid": gid, "fid": fid, "y_pred_lgb": y_pred_lgb,
                                    "public_price": public_price, "population": population,
                                    "altitude": altitude, "emd_nm_k": emd_nm_k, "color": color}, "geometry": geometry})
        except:
            ''

        # existInstalledGEO
        if gfid == None:  # 검색값이 없는 경우
            existInstalledGEO1_param = request.GET.get('existInstalledGEO1')
            existInstalledGEO2_param = request.GET.get('existInstalledGEO2')

            existInstalledGEO_filter = []
            if existInstalledGEO1_param == 'true':
                existInstalledGEO_filter.append(1)
            if existInstalledGEO2_param == 'true':
                existInstalledGEO_filter.append(2)

            existInstalledGEO_object = existInstalledGEO.objects.filter(y_pred_lgb__in=existInstalledGEO_filter)

            if minPrice != None:
                if minPrice != 'null':
                    existInstalledGEO_object = existInstalledGEO_object.filter(public_price__gt=int(minPrice))
            if maxPrice != None:
                if maxPrice != 'null':
                    existInstalledGEO_object = existInstalledGEO_object.filter(public_price__lt=int(maxPrice))

        else:  # 검색값이 있는 경우
            existInstalledGEO_object = existInstalledGEO.objects.filter(Q(gid=gfid) | Q(fid=gfid))
            if existInstalledGEO_object.exists():
                data['ui']['searchData'] = 'existInstalledGEO'

        existInstalledGEO_output = {"features": []}
        for i in existInstalledGEO_object:
            name = i.charging_station_name  # 충전소명
            gid = i.gid  # 충전소명
            fid = i.fid  # 충전소명
            y_pred_lgb = i.y_pred_lgb  # 급완속 여부
            public_price = i.public_price  # 공시지가
            population = i.population  # 인구
            altitude = i.altitude  # 고도
            emd_nm_k = i.emd_nm_k  # 법정동
            address = i.address  # 법정동
            geometry = i.coordinates  # 좌표

            if y_pred_lgb == 1:
                color = '#85FF9E'
            if y_pred_lgb == 2:
                color = '#F29361'
            existInstalledGEO_output['features'].append(
                {"properties": {"name": name, "gid": gid, "fid": fid, "y_pred_lgb": y_pred_lgb,
                                "public_price": public_price, "population": population,
                                "altitude": altitude, "emd_nm_k": emd_nm_k, "color": color, 'address': address},
                 "geometry": geometry})

        # existInstalledGridGEO
        if gfid == None:  # 검색값이 없는 경우
            existInstalledGridGEO_param = request.GET.get('existInstalledGridGEO')

            if existInstalledGridGEO_param == 'true':
                existInstalledGridGEO_object = existInstalledGridGEO.objects.all()

                if minPrice != None:
                    if minPrice != 'null':
                        existInstalledGridGEO_object = existInstalledGridGEO_object.filter(
                            public_price__gt=int(minPrice))
                if maxPrice != None:
                    if maxPrice != 'null':
                        existInstalledGridGEO_object = existInstalledGridGEO_object.filter(
                            public_price__lt=int(maxPrice))

        else:  # 검색값이 있는 경우
            existInstalledGEO_object = existInstalledGEO.objects.filter(Q(gid=gfid) | Q(fid=gfid))
            if existInstalledGEO_object.exists():
                data['ui']['searchData'] = 'existInstalledGEO'
        existInstalledGridGEO_output = {"features": []}
        try:
            for i in existInstalledGridGEO_object:
                name = i.fid
                gid = i.gid  # GID
                fid = i.fid  # GID
                public_price = i.public_price  # 공시지가
                population = i.population  # 인구
                altitude = i.average_altitude  # 고도
                emd_nm_k = i.emd_nm_k  # 법정동
                geometry = i.coordinates
                fast_charging = i.fast_charging

                color = '#EAC435'
                existInstalledGridGEO_output['features'].append(
                    {"properties": {"name": name, "gid": gid, "fid": fid, "y_pred_lgb": fast_charging,
                                    "public_price": public_price, "population": population,
                                    "altitude": altitude, "emd_nm_k": emd_nm_k, "color": color}, "geometry": geometry})
        except:
            ''

        if resultGEO_output != '':
            data['value']['ResultGEO'] = str(json.dumps(resultGEO_output, ensure_ascii=False))
        else:
            data['value']['ResultGEO'] = '[]'

        if recommandGEO_output != '':
            data['value']['RecommandGEO'] = str(json.dumps(recommandGEO_output, ensure_ascii=False))
        else:
            data['value']['RecommandGEO'] = '[]'

        if recommandGSGEO_output != '':
            data['value']['RecommandGSGEO'] = str(json.dumps(recommandGSGEO_output, ensure_ascii=False))
        else:
            data['value']['RecommandGSGEO'] = '[]'

        if resultGEO_output != '':
            data['value']['existInstalledGEO'] = str(json.dumps(existInstalledGEO_output, ensure_ascii=False))
        else:
            data['value']['existInstalledGEO'] = '[]'

        if resultGEO_output != '':
            data['value']['existInstalledGridGEO'] = str(json.dumps(existInstalledGridGEO_output, ensure_ascii=False))
        else:
            data['value']['existInstalledGridGEO'] = '[]'

        return render(request, "marketTools/marketTools.html", context=dict(data=data))
