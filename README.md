# 지훈과얼굴들(jh-faces) 프로젝트
If you are an English user, please scroll down or click [ENG section](https://github.com/JG-Park/jh-faces?tab=readme-ov-file#eng-jh-faces-project).

멀티캠퍼스 멀티잇 데이터 분석 &amp; 엔지니어 34회차 세미프로젝트 3조 '지훈과 얼굴들'의 GitHub 저장소입니다.

- 프로젝트 기간 : 2024/03/07 ~ 2024/03/29  (17 days)
- 분석 목표 : 지리/공간 데이터를 통해 시대 상황을 고려한 전기차 충전소 입지 예측 모델 구현
- 팀원 구성(가나다순) : 박지건, 윤지훈, 이수민, 임예원, 정혜원, 황유진
- 데모페이지 : https://jhfaces.jgpark.kr

![스크린샷1](https://github.com/JG-Park/jh-faces/assets/50548719/0a99b131-8881-4996-9bca-9852cf153b5b)
![스크린샷2](https://github.com/JG-Park/jh-faces/assets/50548719/515657a5-a312-46fa-b5e4-a7c799410fff)


## 개요
- 전기차 충전소에 대한 통합 솔루션 제공
    + 전기차 충전소 실시간 정보(기본정보, 실시간 상태 등)와 위치 정보 제공
    + 전기차 충전소 입지 분석 도구 제공
- Django, MariaDB, Nginx를 Docker Compose로 운영

## 릴리즈 노트

### v0.3b (2024년 4월 1일)
- 시장 분석 도구 추가
  - 새로운 충전소 사이트 추천
  - 다양한 기준에 따른 최적 사이트 추천
  - 기존 충전소에 대한 추가 추천
- UI 개선 
  - 베이스 사이트 UI 통합(base.html)
  - 충전소 정보 페이지 모듈화(main.html)
- CSS 코드 업데이트
- 설정 파일(settings.py, urls.py) 업데이트

### v0.2b (2024년 3월 18일)  
- 전기차 충전소 실시간 정보 버그 수정
- 충전소 세부 페이지 UI 개선
- 사이드바 토글 기능 추가
- 웹사이트 로딩 속도 향상

### v0.1b (2024년 3월 11일)
- 나주시 전기차 충전소 실시간 정보 제공
- 나주시 충전소 기본 정보 및 리스트 제공
- 카카오맵 기반 위치 확인 가능

## 전체 변경 내역
- https://github.com/JG-Park/jh-faces/commits/


---
# [ENG] jh-faces Project

This is the GitHub repository for the JH-Faces('Jihoon and Faces') team, team 3 of the 34th MultiCampus Multi-IT Data Analysis & Engineering Semi-Project.

- Project Period: 2024/03/07 ~ 2024/03/29 (17 days)
- Analysis Goal: Implement a location prediction model for electric vehicle charging stations considering the current situation, using geographic/spatial data.
- Team Members : Carolyne Jung, Jigeon Park, Jihoon Youn, Sumin Lee, Yewon Lim, Yujin Hwang
- Demo Page : https://jhfaces.jgpark.kr

![Screenshot1](https://github.com/JG-Park/jh-faces/assets/50548719/0a99b131-8881-4996-9bca-9852cf153b5b)
![Screenshot2](https://github.com/JG-Park/jh-faces/assets/50548719/515657a5-a312-46fa-b5e4-a7c799410fff)

## Overview
- Provides an integrated solution for electric vehicle charging stations
- Offers real-time information (basic information, real-time status, etc.) and location information for electric vehicle charging stations
- Provides a location analysis tool for electric vehicle charging stations
- Operated using Django, MariaDB, and Nginx through Docker Compose

## Release Notes

### v0.3b (April 1, 2024)
- Added market analysis tool
- Recommendations for new charging station sites
- Best recommended sites based on various criteria
- Additional recommendations for existing stations
- Enhanced UI
  - Consolidated base site UI into base.html
  - Modularized station information page (main.html)
- Updated CSS code
- Updated configuration files (settings.py, urls.py)

### v0.2b (March 18, 2024)
- Fixed a bug causing errors when fetching real-time information from electric vehicle charging stations
- Improved UI of the charging station detail page
- Added a sidebar toggle function
- Enhanced website loading speed

### v0.1b (March 11, 2024)
- Provided real-time information on electric vehicle charging stations in Naju-si
- Provided basic information and list of charging stations in Naju-si
- Enabled location checking based on Kakao Map

## Full Changelog
- https://github.com/JG-Park/jh-faces/commits/
