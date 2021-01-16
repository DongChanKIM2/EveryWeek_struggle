# 날씨의 지역을 입력값으로 출력하는 프로그램 만들기

import requests

#location = 'seoul'
location = input("도시명을 영어로 입력하세요: ")

get_woeid_url = f'https://www.metaweather.com//api/location/search/?query={location}'

response = requests.get(get_woeid_url).json()
id = response[0]['woeid']

url = f'https://www.metaweather.com/api/location/{id}/'

response_url=requests.get(url).json()

celsius = response_url['consolidated_weather'][0]['the_temp']
Fahrenheit = celsius*1.8 + 32

print(f'오늘의 섭씨는 {celsius:.2f}도 이고, 화씨는 {Fahrenheit:.2f}도 입니다.')