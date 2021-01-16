#무작위 나이 생성기
import requests

url = 'https://api.agify.io?name=mecha'

response = requests.get(url).json()

# 출력결과: 내 이름은 mecha, 나이는 27
response['age']=27
print(response)
# ", ' 각각 다르게 인식됨 -> f-string에서 중요
print(f"내 이름은 {response['name']}, 나이는 {response['age']}")
