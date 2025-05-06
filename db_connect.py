## DB 연동하기
import pandas as pd
from sqlalchemy import create_engine

csv_filename = "7_weather.csv"

df = pd.read_csv(csv_filename)

# 날짜 타입 전처리
# 날짜 끝에 마침표 제거
df['날짜'] = df['날짜'].str.rstrip('.')  # 또는 str.replace(r'\.$', '', regex=True)

# 연도 붙여서 날짜 형식으로 변환
df['날짜'] = pd.to_datetime('2025.' + df['날짜'], format='%Y.%m.%d')

# 날짜 문자열을 datetime으로 변환 (가독성 향상용)
df = df.dropna(subset=['날짜'])  # 날짜 파싱 실패한 행 제거

# 🔐 여기에 너의 MariaDB 접속 정보 입력
user = 'root'
password = "비밀번호 입력"
host = 'IP'   
port = 3306
db_name = 'de_1_weather' # HeidiSQL에서 미리 만든 DB 이름

# SQLAlchemy 엔진 생성 (MariaDB도 mysql로 접속함!)
db_url = f'mysql+pymysql://{user}:{password}@{host}:{port}/{db_name}'
engine = create_engine(db_url, echo=True)

from sqlalchemy import text

# 기존 날짜 삭제
with engine.begin() as conn:
    for date in df['날짜'].unique():
        conn.execute(text("DELETE FROM weather WHERE 날짜 = :date"), {"date": date})

# 새 데이터 삽입
df.to_sql('weather_7', con=engine, if_exists='append', index=False)

print("✅ MariaDB에 데이터 저장 완료!")
