import requests

#접근키
bot_token = '1561659025:AAFj96HSvwU84QDvTydidydjLVfsFTlUSG8'
#'내' 정보
me = '1592550513'

client_ID = 'C8UVbbnUAGxU2ASU3ZIC'
client_secret = 'guyxEgnEyV'
headers = {
    'X-Naver-Client-Id': client_ID,
    'X-Naver-Client-Secret': client_secret
}

query = 'ps5'
display = 100
end = 30
start = 1
naver_url=f'https://openapi.naver.com/v1/search/shop.json?query={query}&display={display}&start={start}'

response = requests.get(naver_url, headers=headers).json()

price_list = []
link_list=[]

for i in range(0,end):
    item = response['items'][i]['lprice']
    link = response['items'][i]['link']
    price_list.append(item)
    link_list.append(link)

price_list = list(map(int, price_list))
average_price = sum(price_list)/len(price_list)
minimum_average_price = int(average_price * 0.7)
maximum_average_price = int(average_price * 1.5)

refined_price_list = []
refined_link_list=[]

for i in range(0,end):
    if price_list[i] >= minimum_average_price and price_list[i] <= maximum_average_price:
       refined_price_list.append(price_list[i])
       refined_link_list.append(link_list[i])
print(refined_price_list)

price_list = list(map(int, refined_price_list))
lowest_index = refined_price_list.index(min(refined_price_list))

print(refined_price_list[lowest_index])
print(refined_link_list[lowest_index])


"""
message = f"{item['title']}\n{item['lprice']}\n{item['link']}"

message_url =f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={me}&text={message}'
response=requests.get(message_url)
"""