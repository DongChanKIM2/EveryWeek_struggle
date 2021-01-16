# programmed_weather를 module화 시켜 import해서 main.py 작성
# from이 아니라 import weekly_weather만 하면 weekly_weather.fetch_weather_infos()로 써야되서 매우 귀찮!
from weekly_weather import fetch_weather_infos
#, get_farenheit

location = input('도시명을 영어로 입력하세요 1)seoul, 2)busan: ') 

for weather_info in fetch_weather_infos(location):
    print(f"{weather_info['min_temp']}°C & {weather_info['max_temp']}°C")
