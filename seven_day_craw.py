#라이브러리 할당
from selenium import webdriver
import time
import csv
import re
from selenium.webdriver.common.by import By

# 저장할 csv 파일 이름
csv_filename = "C:/Users/seoyeon/PycharmProjects/data_engenius/weather_data/7_weather.csv"

# 브라우저 한 번만 열기
browser = webdriver.Chrome()

browser.get("https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8&oquery=%EB%82%A0%EC%94%A8&tqi=i%2BpOadqo1e8ssjCCWWGssssst2R-424200")
time.sleep(2)

# 현재 창의 높이를 가져와서 스크롤 내리기
current_height = browser.execute_script("return window.innerHeight;")
browser.execute_script(f"window.scrollTo(0, {current_height});")


# 크롤링 하는 코드 짜야함
# 7일치 날씨 정보가 담긴 부분 크롤링
weather_blocks = browser.find_elements(By.CSS_SELECTOR, 'ul.week_list > li')

date_list = []
highest_list = []
lowest_list = []
am_rain_list = []
pm_rain_list = []


for block in weather_blocks:
    try:
        date = block.find_element(By.CSS_SELECTOR, 'span.date').text.strip()
        temp_high = block.find_element(By.CSS_SELECTOR, 'span.highest').text.strip()
        temp_low = block.find_element(By.CSS_SELECTOR, 'span.lowest').text.strip()
        rain_spans = block.find_elements(By.CSS_SELECTOR, 'span.rainfall')
        if len(rain_spans) >= 2:
            am_rain = rain_spans[0].text.strip()
            pm_rain = rain_spans[1].text.strip()
        else:
            am_rain = pm_rain = "정보 없음"


        am_rain_num = int(re.findall(r'\d+', am_rain)[0])
        pm_rain_num = int(re.findall(r'\d+', pm_rain)[0])
        lowest = int(re.findall(r'\d+', temp_low)[0])
        highest = int(re.findall(r'\d+', temp_high)[0])

        date_list.append(date)
        am_rain_list.append(am_rain_num)
        pm_rain_list.append(pm_rain_num)
        lowest_list.append(lowest)
        highest_list.append(highest)


    except Exception as e:
        # print(f"Error on {date}: {e}")
        continue

# 결과 확인
print(date_list)
print(am_rain_list)
print(pm_rain_list)
print(lowest_list)
print(highest_list)

# 크롤링한 데이터를 CSV 파일에 추가 저장
with open(csv_filename, mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # 파일이 비어 있는 경우, 헤더 추가
    if file.tell() == 0:
        writer.writerow(["날짜", "오전 강수 확률", "오후 강수 확률", "최저 온도", "최고 온도"])  # 컬럼명 추가

    # 새로운 데이터 추가
    for i in range(7):
        writer.writerow([date_list[i], am_rain_list[i], pm_rain_list[i], lowest_list[i], highest_list[i]])

print(f"크롤링한 데이터 {csv_filename} 파일에 추가 저장 완료")
