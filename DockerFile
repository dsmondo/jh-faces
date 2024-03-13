# Dockerfile
FROM python:3.11

ENV PYTHONUNBUFFERED 1

# /src 폴더 생성 대신 WORKDIR 명령어를 사용하여 작업 디렉토리 설정 및 필요시 생성
WORKDIR /src

# 상대 경로를 사용하지 않고, 현재 컨텍스트의 파일을 직접 참조
COPY requirements.txt /src/
RUN pip install -r requirements.txt

# 현재 컨텍스트의 모든 파일과 폴더를 /src/ 안으로 복사
COPY . /src/
