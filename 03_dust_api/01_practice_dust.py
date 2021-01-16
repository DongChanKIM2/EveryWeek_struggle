# API란? Application programming interface

import requests
#from bs4 import BeautifulSoup

#공공데이터 포털에서 미세먼지 발급받은 Key
key = 'WXDl24tvvD09fnWNuDgF4V8aLbEmMnhR%2Frmvi4mfSqLNvZkR6SufET7w6R4wR249Sxa3kzPz0aJ22XtN5wacHg%3D%3D'
# url : f + 주소 + 서비스키 + 행수(더 받을수도 있음) + 페이지수 + 지역 + 버전 + 리턴타입
url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&numOfRows=5&pageNo=1&sidoName=서울&ver=1.0&returnType=json'

# json / csv / txt 데이터 본질은 같으나 json은 javascript 객체라서 요새 많이 사용
response = requests.get(url).json()

print(url)
print(response)
print(type(response))

# 특정 데이터 추출
print(response['response']['body']['items'][3]['stationName'])
