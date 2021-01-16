import requests

# def info out(location in)
# fetch는 인터넷에서 연결된 상태에서 '당겨오다'라는 의미
def fetch_weather_infos(location):
    woeid_url = f'https://www.metaweather.com/api/location/search/?query={location}'
    response = requests.get(woeid_url).json()
    woeid = response[0]['woeid']

    weather_url = f'https://www.metaweather.com/api/location/{woeid}/'
    response = requests.get(weather_url).json()
    return response['consolidated_weather'] #[]을 return


# 섭씨 in => 화씨 out
def get_farenheit(celscius):
    return (celscius * 1.8) + 32

