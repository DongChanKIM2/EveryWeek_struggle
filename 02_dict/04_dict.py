# dic는 표의 행/열을 바꿔 코드로 옮기기 위한 것
# key(1:1 관계) 여러개들을 모아 하나의 dic 생성

my_home = {
    'location': '서울',
    'dust': 10,
    'temp': 5
}
print(my_home['dust'])


weather_infos = {
    '지역': ['서울', '부산', '대구'],
    '미세먼지': [59, 30, 28],
    '온도': [-4, 0, -2],
    '습도': [70, 50, 30]
}
print(weather_infos)