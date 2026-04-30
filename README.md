# 🌦️ Weather Data Pipeline: 자동 크롤링, DB 적재 및 시각화 시스템

본 프로젝트는 네이버 날씨 데이터를 자동으로 수집(Crawling)하여 MariaDB에 적재(ETL)하고, 저장된 데이터를 바탕으로 기온 및 강수 확률을 시각화하는 **데이터 엔지니어링 파이프라인 구축** 프로젝트입니다.

## 👤member
- **전서연** (서울여대 데이터사이언스학과 23학번)
- **조연우** (서울여대 데이터사이언스학과 23학번)
- **권수영** (서울여대 데이터사이언스학과 24학번)


## 📌 프로젝트 개요
- **주제**: 데이터 분석을 위한 데이터베이스 자동화 시스템 구축
- **기간**: 2025년 상반기
- **참여 인원**: 전서연, 권수영, 조연우 (지도교수: 이병걸 교수님)
- **주요 기능**: 
    - **Web Scraping**: Selenium을 활용한 네이버 날씨(7일 예보) 데이터 실시간 수집
    - **Data Pipeline**: Pandas 전처리 후 SQLAlchemy를 통해 MariaDB에 자동 데이터 적재
    - **Visualization**: Seaborn 및 Matplotlib을 활용한 기온 추이 및 강수 확률 시각화 대시보드
    - **Automation**: Windows Task Scheduler를 활용한 정기 데이터 갱신 구조 설계

## 🛠️ 기술 스택
- **Language**: `Python 3.x`
- **Libraries**: `Selenium`, `Pandas`, `SQLAlchemy`, `PyMySQL`, `Matplotlib`, `Seaborn`
- **Database**: `MariaDB` (HeidiSQL)
- **Environment**: `PyCharm`, `Windows Task Scheduler`

## 📂 파일 구조 및 설명
- `seven_day_craw.py`: Selenium 기반 날씨 데이터 크롤링 스크립트 (CSV 저장)
- `db_connect.py`: 수집된 데이터를 MariaDB 형식에 맞춰 전처리 및 적재하는 스크립트
- `visualization.py`: DB에서 데이터를 호출하여 시각화 그래프를 생성하는 코드
- `craw_db_connect.py`: **[통합본]** 수집부터 적재, 시각화까지 전 과정을 수행하는 메인 파이프라인
- `7_weather.csv`: 스크래핑 결과 데이터 샘플

## 🚀 시작하기

### 1. 데이터베이스 준비
MariaDB에 접속하여 데이터를 저장할 데이터베이스를 생성합니다.
```sql
CREATE DATABASE de_1_weather;
