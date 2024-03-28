
from .models import ResultGEO  # 알맞은 경로로 수정해주세요.
from .models import RecommandGEO
from .models import RecommandGSGEO  # 알맞은 경로로 수정해주세요.
from .models import existInstalledGEO
from .models import existInstalledGridGEO

import json
def migrate_ResultGEO(file_path):
    # JSON 파일 열기 및 파싱
    with open(file_path, 'r') as file:
        data = json.load(file)

    # 각 Feature에 대해 반복
    for feature in data['features']:
        properties = feature['properties']
        # 모델 인스턴스 생성
        result_geo = ResultGEO(
            unnamed_0=properties.get('Unnamed: 0'),
            fid=properties.get('fid'),
            gid=properties.get('gid'),
            emd_cd=properties.get('emd_cd'),
            emd_nm_k=properties.get('emd_nm_k'),
            charging_station_accessibility=properties.get('충전소접근성'),
            gas_station_count=properties.get('주유소_수'),
            charging_station_count=properties.get('충전소_수'),
            performance_facility_accessibility=properties.get('공연시설접근성'),
            public_price=properties.get('공시지가'),
            library_accessibility=properties.get('도서관접근성'),
            hospital_accessibility=properties.get('병원접근성'),
            health_center_accessibility=properties.get('보건기관접근성'),
            community_park_accessibility=properties.get('생활권공원접근성'),
            fire_station_accessibility=properties.get('소방서접근성'),
            population=properties.get('인구'),
            theme_park_accessibility=properties.get('주제공원접근성'),
            parking_lot_accessibility=properties.get('주차장접근성'),
            sports_facility_accessibility=properties.get('체육시설접근성'),
            elementary_school_accessibility=properties.get('초등학교접근성'),
            fast_charging=properties.get('급/완속여부'),
            agricultural_area=properties.get('농림지역'),
            altitude=properties.get('고도'),
            river=properties.get('하천'),
            center_coordinates=properties.get('중심좌표'),
            y_pred_rf=properties.get('y_pred_rf'),
            y_pred_lgb=properties.get('y_pred_lgb'),
            y_pred_xgb=properties.get('y_pred_xgb'),
            y_pred_voting=properties.get('y_pred_voting'),
            cluster_id=properties.get('CLUSTER_ID'),
            cluster_size=properties.get('CLUSTER_SIZE'),
            coordinates=feature['geometry']  # 'geometry' 데이터 저장
        )
        # 데이터베이스에 저장
        result_geo.save()

def migrate_RecommandGEO(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    # 각 Feature에 대해 반복
    for feature in data['features']:
        properties = feature['properties']
        # 모델 인스턴스 생성
        recommand_geo = RecommandGEO(
            unnamed_0=properties.get('Unnamed: 0'),
            fid=properties.get('fid'),
            gid=properties.get('gid'),
            emd_cd=properties.get('emd_cd'),
            emd_nm_k=properties.get('emd_nm_k'),
            charging_station_accessibility=properties.get('충전소접근성'),
            gas_station_count=properties.get('주유소_수'),
            charging_station_count=properties.get('충전소_수'),
            performance_facility_accessibility=properties.get('공연시설접근성'),
            public_price=properties.get('공시지가'),
            library_accessibility=properties.get('도서관접근성'),
            hospital_accessibility=properties.get('병원접근성'),
            health_center_accessibility=properties.get('보건기관접근성'),
            community_park_accessibility=properties.get('생활권공원접근성'),
            fire_station_accessibility=properties.get('소방서접근성'),
            population=properties.get('인구'),
            theme_park_accessibility=properties.get('주제공원접근성'),
            parking_lot_accessibility=properties.get('주차장접근성'),
            sports_facility_accessibility=properties.get('체육시설접근성'),
            elementary_school_accessibility=properties.get('초등학교접근성'),
            fast_charging=properties.get('급/완속여부'),
            agricultural_area=properties.get('농림지역'),
            altitude=properties.get('고도'),
            river=properties.get('하천'),
            center_coordinates=properties.get('중심좌표'),
            y_pred_rf=properties.get('y_pred_rf'),
            y_pred_lgb=properties.get('y_pred_lgb'),
            y_pred_xgb=properties.get('y_pred_xgb'),
            y_pred_voting=properties.get('y_pred_voting'),
            cluster_id=properties.get('CLUSTER_ID'),
            cluster_size=properties.get('CLUSTER_SIZE'),
            coordinates=feature['geometry'],  # 'geometry' 데이터 저장
            # 새로운 필드 값 할당
            type=properties.get('유형'),
            detailed_category=properties.get('상세분류'),
            district_code=properties.get('시군구코드'),
            road_name_code=properties.get('도로명코드'),
            road_address=properties.get('도로명주소'),
            institution_name=properties.get('기관명'),
            position_x=properties.get('위치X'),
            position_y=properties.get('위치Y')
        )
        # 데이터베이스에 저장
        recommand_geo.save()


def migrate_RecommandGSGEO(file_path):
    # 파일 열기
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # 각 feature에 대해 반복
    for feature in data['features']:
        properties = feature['properties']

        # 중심좌표 처리
        center_point = str(properties['중심좌표'])

        # 모델 인스턴스 생성
        instance = RecommandGSGEO(
            unnamed_0=properties.get('Unnamed: 0'),
            fid=properties.get('fid'),
            gid=properties.get('gid'),
            emd_cd=properties.get('emd_cd'),
            emd_nm_k=properties.get('emd_nm_k'),
            charging_station_accessibility=properties.get('충전소접근성'),
            gas_station_count=properties.get('주유소_수'),
            charging_station_count=properties.get('충전소_수'),
            performance_facility_accessibility=properties.get('공연시설접근성'),
            public_price=properties.get('공시지가'),
            library_accessibility=properties.get('도서관접근성'),
            hospital_accessibility=properties.get('병원접근성'),
            health_center_accessibility=properties.get('보건기관접근성'),
            community_park_accessibility=properties.get('생활권공원접근성'),
            fire_station_accessibility=properties.get('소방서접근성'),
            population=properties.get('인구'),
            theme_park_accessibility=properties.get('주제공원접근성'),
            parking_lot_accessibility=properties.get('주차장접근성'),
            sports_facility_accessibility=properties.get('체육시설접근성'),
            elementary_school_accessibility=properties.get('초등학교접근성'),
            fast_charging=properties.get('급/완속여부'),
            agricultural_area=properties.get('농림지역'),
            altitude=properties.get('고도'),
            river=properties.get('하천'),
            center_coordinates=center_point,  # GeoDjango의 fromstr 함수를 사용해 WKT에서 Point 객체로 변환
            y_pred_rf=properties.get('y_pred_rf'),
            y_pred_lgb=properties.get('y_pred_lgb'),
            y_pred_xgb=properties.get('y_pred_xgb'),
            y_pred_voting=properties.get('y_pred_voting'),
            cluster_id=properties.get('CLUSTER_ID'),
            cluster_size=properties.get('CLUSTER_SIZE'),
            gas_station_name=properties.get('주유소/충전소명'),
            address_jibun=properties.get('소재지지번주소'),
            longitude=properties.get('Longitude'),
            latitude=properties.get('Latitude'),
        )

        # 데이터베이스에 저장
        instance.save()
def migrate_existInstalledGEO(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    for feature in data['features']:
        properties = feature['properties']

        exist_installed_geo = existInstalledGEO(
            unnamed_0=properties.get('Unnamed: 0'),
            installation_year=properties.get('설치년도'),
            address=properties.get('주소'),
            charging_station_name=properties.get('충전소명'),
            facility_category_major=properties.get('시설구분(대)'),
            facility_category_minor=properties.get('시설구분(소)'),
            model_type_major=properties.get('기종(대)'),
            model_type_minor=properties.get('기종(소)'),
            operating_org_major=properties.get('운영기관(대)'),
            operating_org_minor=properties.get('운영기관(소)'),
            charger_type=properties.get('충전기타입'),
            user_restriction=properties.get('이용자제한'),
            charger_id=properties.get('충전기ID'),
            charging_station_id=properties.get('충전소ID'),
            latitude=properties.get('위도'),
            longitude=properties.get('경도'),
            fid=properties.get('fid'),
            gid=properties.get('gid'),
            emd_cd=properties.get('emd_cd'),
            emd_nm_k=properties.get('emd_nm_k'),
            charging_station_accessibility=properties.get('충전소접근성'),
            gas_station_count=properties.get('주유소_수'),
            charging_station_count=properties.get('충전소_수'),
            performance_facility_accessibility=properties.get('공연시설접근성'),
            public_price=properties.get('공시지가'),
            library_accessibility=properties.get('도서관접근성'),
            hospital_accessibility=properties.get('병원접근성'),
            health_center_accessibility=properties.get('보건기관접근성'),
            community_park_accessibility=properties.get('생활권공원접근성'),
            fire_station_accessibility=properties.get('소방서접근성'),
            population=properties.get('인구'),
            theme_park_accessibility=properties.get('주제공원접근성'),
            parking_lot_accessibility=properties.get('주차장접근성'),
            sports_facility_accessibility=properties.get('체육시설접근성'),
            elementary_school_accessibility=properties.get('초등학교접근성'),
            fast_charging=properties.get('급/완속여부'),
            agricultural_area=properties.get('농림지역'),
            altitude=properties.get('고도'),
            river=properties.get('하천'),
            center_coordinates=properties.get('중심좌표'),
            y_pred_rf=properties.get('y_pred_rf', None),
            y_pred_lgb=properties.get('y_pred_lgb', None),
            y_pred_xgb=properties.get('y_pred_xgb', None),
            y_pred_voting=properties.get('y_pred_voting', None),
            cluster_id=properties.get('CLUSTER_ID', None),
            cluster_size=properties.get('CLUSTER_SIZE', None),
            coordinates=feature['geometry']
        )
        exist_installed_geo.save()
def migrate_existInstalledGridGEO(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    for feature in data['features']:
        properties = feature['properties']

        exist_installed_grid_geo = existInstalledGridGEO(
            unnamed_0=properties.get('Unnamed: 0'),
            fid=properties['fid'],
            gid=properties['gid'],
            emd_cd=properties['emd_cd'],
            emd_nm_k=properties['emd_nm_k'],
            charging_station_accessibility=properties['충전소접근성'],
            gas_station_count=properties['주유소_수'],
            charging_station_count=properties['충전소_수'],
            performance_facility_accessibility=properties['공연시설접근성'],
            public_price=properties['공시지가'],
            library_accessibility=properties['도서관접근성'],
            hospital_accessibility=properties['병원접근성'],
            health_center_accessibility=properties['보건기관접근성'],
            community_park_accessibility=properties['생활권공원접근성'],
            fire_station_accessibility=properties['소방서접근성'],
            population=properties['인구'],
            theme_park_accessibility=properties['주제공원접근성'],
            parking_lot_accessibility=properties['주차장접근성'],
            sports_facility_accessibility=properties['체육시설접근성'],
            elementary_school_accessibility=properties['초등학교접근성'],
            fast_charging=properties['급/완속여부'],
            agricultural_area=properties['농림지역'],
            average_altitude=properties['평균고도'],
            river=properties['하천'],
            center_coordinates=properties['중심좌표'],
            coordinates=feature['geometry']
        )
        exist_installed_grid_geo.save()