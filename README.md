# 🌦️ Weather Data Pipeline: 자동 크롤링, DB 적재 및 시각화 시스템

*본 프로젝트는 데이터 엔지니어링 기초 역량 강화 및 효율적인 데이터 관리 시스템 설계를 목적으로 수행되었습니다.*

본 프로젝트는 네이버 날씨 데이터를 자동으로 수집(Crawling)하여 MariaDB에 적재(ETL)하고, 저장된 데이터를 바탕으로 기온 및 강수 확률을 시각화하는 **데이터 엔지니어링 파이프라인 구축** 프로젝트입니다.

## 👤member
- **전서연** (서울여대 데이터사이언스학과 23학번)
- **조연우** (서울여대 데이터사이언스학과 23학번)
- **권수영** (서울여대 데이터사이언스학과 24학번)


## 📌 프로젝트 개요
- **주제**: 데이터 분석을 위한 데이터베이스 자동화 시스템 구축
- **기간**: 2025년 3월~5월
- **참여 인원**: 전서연, 권수영, 조연우 (지도교수: 이병걸 교수님)
- **참고 자료**
- [데이터엔지니어스 티스토리 : 주제 선정 및 소개 자료](https://dataengenius.tistory.com/96)
- [데이터엔지니어스 티스토리 : 최종 결과](https://dataengenius.tistory.com/211)
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
```

### 2. 라이브러리 설치
프로젝트 실행에 필요한 파이썬 라이브러리를 설치합니다.
```
pip install selenium pandas sqlalchemy pymysql matplotlib seaborn
```

### 3. 접속 정보 설정
craw_db_connect.py 파일 내의 user, password, host 정보를 본인의 로컬 DB 환경에 맞춰 수정합니다.

### 4. 실행
```
python craw_db_connect.py
```

## 📊 데이터 분석 및 시각화 결과
- **기온 변화 분석** : 날짜별 최저/최고 기온을 꺾은선 그래프로 시각화하여 일교차 및 기온 변화 추이를 한눈에 파악할 수 있습니다.
- **강수 확률 분석** : 오전과 오후의 강수 확률을 막대 그래프로 비교하여 기상 변화를 예측합니다.

## 📝 연구 요약 및 시사점
- **시스템 의의** : 수동 데이터 수집의 번거러움을 해결하고, 모듈화된 구조를 통해 향후 AI기반 기상 예측 모델과의 통합 가능성을 열어두었습니다.
- **한계 및 향후 과제**: 로컬 환경(Window 스케줄러 & MacOS의 터미널)의 물리적 제약을 극복하기 위해 향후 클라우드 서버(AWS/GCP) 기반의 인프라 구축 및 Docker 컨테이너 도입이 필요합니다.

