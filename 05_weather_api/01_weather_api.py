# 도시의 오늘 현재 온도를 섭씨(cel)와 화씨(Fahren)로 출력

import requests

url=f'https://www.metaweather.com/api/location/1132599/'

response = requests.get(url).json()

print(url)
#print(response)

""" 이번 주 날씨 전체 불러오기
weather_infos = response['consolidated_weather']
weather_today = weather_infos[0] """

# 함수 및 변수는 앞글자도 무조건 소문자 사용
celsius = response['consolidated_weather'][0]['the_temp']
fahrenheit = celsius*1.8 + 32

print(f'오늘의 섭씨는 {celsius:.2f}도 이고, 화씨는 {fahrenheit:.2f}도 입니다.')