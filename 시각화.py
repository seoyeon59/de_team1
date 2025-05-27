import pandas as pd
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 윈도우 기본 한글 폰트 설정 (맑은 고딕)
font_path = "C:/Windows/Fonts/malgun.ttf"  # 윈도우 경로, 한글 폰트 위치
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# 마이너스 기호 깨지는 문제 해결
plt.rcParams['axes.unicode_minus'] = False

# CSV 불러오기
df = pd.read_csv('naver_weather.csv')

# 1) 날짜 문자열 끝에 있는 점(.) 제거
df['date'] = df['date'].str.rstrip('.')

# 2) 점(.) 기준으로 월과 일을 분리해서 두 개의 새 컬럼 만들기
df[['month', 'day']] = df['date'].str.split('.', expand=True)

# 3) 연도 붙여서 날짜 문자열 새로 만들기 (월, 일이 한 자리면 0 채우기)
df['date'] = '2025-' + df['month'].str.zfill(2) + '-' + df['day'].str.zfill(2)

# 4) datetime 타입으로 변환
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')


# 기온에서 '°' 제거 후 숫자형 변환
df['low'] = df['low'].str.replace('°', '').astype(int)
df['high'] = df['high'].str.replace('°', '').astype(int)

# 강수확률에서 '%' 제거 후 숫자형 변환
df['morning_rainfall'] = df['morning_rainfall'].str.replace('%', '').astype(int)
df['afternoon_rainfall'] = df['afternoon_rainfall'].str.replace('%', '').astype(int)

# 그래프 그리기
plt.figure(figsize=(12, 6))

plt.plot(df['date'], df['low'], label='최저기온', marker='o')
plt.plot(df['date'], df['high'], label='최고기온', marker='o')

plt.bar(df['date'] - pd.Timedelta(days=0.2), df['morning_rainfall'], width=0.4, label='오전 강수확률', alpha=0.5)
plt.bar(df['date'] + pd.Timedelta(days=0.2), df['afternoon_rainfall'], width=0.4, label='오후 강수확률', alpha=0.5)

plt.title('날짜별 기온 및 강수확률')
plt.xlabel('날짜')
plt.ylabel('기온 (°C) / 강수확률 (%)')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
