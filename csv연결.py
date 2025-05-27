import pandas as pd
import mysql.connector
from mysql.connector import Error

csv_file_path = 'naver_weather.csv'
df = pd.read_csv(csv_file_path)

# 날짜 변환 (2025년으로 임의 지정)
df['date'] = pd.to_datetime('2025-' + df['date'], format='%Y-%m.%d.').dt.strftime('%Y-%m-%d')

# %와 ° 제거 후 숫자형 변환
df['morning_rainfall'] = df['morning_rainfall'].str.replace('%', '').astype(int)
df['afternoon_rainfall'] = df['afternoon_rainfall'].str.replace('%', '').astype(int)
df['low'] = df['low'].str.replace('°', '').astype(int)
df['high'] = df['high'].str.replace('°', '').astype(int)

connection = None  # 미리 None으로 초기화

try:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='dnduswh12',
        database='weadata'
    )

    if connection.is_connected():
        print("MySQL 연결 성공!")

        cursor = connection.cursor()

        for index, row in df.iterrows():
            sql = """
            INSERT INTO weather (date, morning_rainfall, afternoon_rainfall, low, high)
            VALUES (%s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE 
                morning_rainfall = VALUES(morning_rainfall),
                afternoon_rainfall = VALUES(afternoon_rainfall),
                low = VALUES(low),
                high = VALUES(high)
            """
            values = (row['date'], row['morning_rainfall'], row['afternoon_rainfall'], row['low'], row['high'])
            cursor.execute(sql, values)

        connection.commit()
        print("CSV 데이터가 MySQL에 성공적으로 삽입되었습니다.")

except Error as e:
    print(f"에러 발생: {e}")

finally:
    if connection and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL 연결 종료.")

