import requests

#접근키
bot_token = '1561659025:AAFj96HSvwU84QDvTydidydjLVfsFTlUSG8'

# 내 id를 확인하기 위한 URL
update_url = f'https://api.telegram.org/bot{bot_token}/getupdates'

#'내' 정보
me = '1592550513'

# 로또 번호 추첨기
# 1~45 중 6개를 뽑는다
import random

message = random.sample(range(1,46), 6)

# message를 보낼 URL
message_url =f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={me}&text={message}'

# 1번방법으로 링크 클릭 -> 브라우저 검색

# 2번 방법으로 requests
response=requests.get(message_url)

# 나는 requests(요청)까지 한거고 나머지는 텔레그렘이 (respond)응답한거야
# client <-> server 의 관계는 요청함 <-> 응답함과 동일함
