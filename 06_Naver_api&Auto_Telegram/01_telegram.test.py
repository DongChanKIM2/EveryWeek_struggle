import requests

#접근키
bot_token = '1561659025:AAFj96HSvwU84QDvTydidydjLVfsFTlUSG8'

# 내 id를 확인하기 위한 URL
update_url = f'https://api.telegram.org/bot{bot_token}/getupdates'

#'내' 정보
me = '1592550513'

# message
message = "Hello startcamp"

# message를 보낼 URL
message_url =f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={me}&text={message}'

# 정보를 검색하기 위한 방법으로 두 가지가 있다
# 1번 방법으로 링크 클릭하는 것은 브라우저 검색하는 것과 동일(검색창은 껍데기에 불과하고 사실 주소창이 본체야)
# 주소창에 주소가 길지만 실제 검색하는 기능은 매우 적음 / 검색과 무관한 것들은 지워도 검색 잘 돼!
# 2번 방법으로 requests(매우 강력함)
response=requests.get(message_url)

# 나는 requests(요청)까지 한거고 나머지는 텔레그렘이 (respond)응답한거야
# client <-> server 의 관계는 요청함 <-> 응답함과 동일함
