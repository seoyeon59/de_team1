from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

# Chrome 드라이버 실행
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 네이버 날씨 페이지 열기
url = 'https://weather.naver.com/'
browser.get(url)

# 스크롤하여 모든 날짜 보이게 하기
time.sleep(3)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)

weather_data = []

# 1~2일차 수집
for i in range(1, 3):  # 1, 2
    try:
        base = f"#weekly > ul > li:nth-child({i})"

        date = browser.find_element(By.CSS_SELECTOR, f"{base} > div > div.cell_date > span > span").text.strip()

        morning = browser.find_element(By.CSS_SELECTOR, f"{base} > div > div.cell_weather > span:nth-child(1) > strong > span.rainfall").text.strip().split('\n')[-1]
        afternoon = browser.find_element(By.CSS_SELECTOR, f"{base} > div > div.cell_weather > span:nth-child(2) > strong > span.rainfall").text.strip().split('\n')[-1]

        low = browser.find_element(By.CSS_SELECTOR, f"{base} > div > div.cell_temperature > strong > span.lowest").text.strip().split('\n')[-1]
        high = browser.find_element(By.CSS_SELECTOR, f"{base} > div > div.cell_temperature > strong > span.highest").text.strip().split('\n')[-1]

        weather_data.append({
            'date': date,
            'morning_rainfall': morning,
            'afternoon_rainfall': afternoon,
            'low': low,
            'high': high
        })

    except Exception as e:
        print(f"{i}일차 오류: {e}")

# 3~7일차 수집
for i in range(3, 8):
    try:
        base = f"#weekly > div.scroll_control > div > ul > li:nth-child({i})"

        # 날짜 처리 (두 줄 텍스트: 요일 + 날짜)
        date_raw = browser.find_element(By.CSS_SELECTOR, f"{base} > div > div > div.cell_date").text.strip().split('\n')
        if len(date_raw) == 2:
            weekday, date = date_raw
        elif len(date_raw) == 1:
            weekday, date = "", date_raw[0]
        else:
            continue  # 잘못된 항목 skip

        if date == "":
            continue

        # 강수확률
        rainfall_tags = browser.find_elements(By.CSS_SELECTOR, f"{base} span.rainfall")
        morning = rainfall_tags[0].text.strip().split('\n')[-1] if len(rainfall_tags) > 0 else "정보 없음"
        afternoon = rainfall_tags[1].text.strip().split('\n')[-1] if len(rainfall_tags) > 1 else "정보 없음"

        # 기온
        low = browser.find_element(By.CSS_SELECTOR, f"{base} span.lowest").text.strip().split('\n')[-1]
        high = browser.find_element(By.CSS_SELECTOR, f"{base} span.highest").text.strip().split('\n')[-1]

        weather_data.append({
            'date': date,
            'morning_rainfall': morning,
            'afternoon_rainfall': afternoon,
            'low': low,
            'high': high
        })

    except Exception as e:
        print(f"{i}일차 오류: {e}")

# 결과 출력
for day in weather_data:
    print(day['date'])
    print(day['morning_rainfall'])
    print(day['afternoon_rainfall'])
    print(day['low'])
    print(day['high'])
    print('-' * 30)

# csv 파일 저장
df = pd.DataFrame(weather_data)
df.to_csv('naver_weather.csv', index=False, encoding='utf-8-sig')


print("CSV 파일 저장 완료: naver_weather.csv")

# 브라우저 종료
browser.quit()