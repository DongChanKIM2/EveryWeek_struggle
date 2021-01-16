# 1st week summary

## 0. Background Setting
- Python & Jupyter Notebook 설치
- Git 설치
  - 처음 설치:  https://git-scm.com/download/win
  - 설치된 경우: 업데이트 진행 git update-git-for-windows
- VS Code 설치
  - 확장 프로그램: Python, Korean
  - 터미널: Git Bash
- Typora 설치
  - 마크다운 편집기
  - 문법, list, code block, Image and link, Table

## 1. Git Bash
- 폴더 상징 특수기호
- 명령어(01_basic_md 참조)

## 2. VS code
- Use Git Bash 명령어 in VS Code 
- dict
- Weather API
- Main 모듈
- Telegram & Naver API & PythonAnywhere

### 2.1 Telegram 작동 방법
- 구성요소: 내 컴퓨터(Client) / Telegram(Server)
- 작동방식: API에서 정보를 requests(요청)한 것처럼 request하면 텔레그렘이 respond(응답함)
	- 필요한 것
		- 내 bot에 접근하기 위한 key(Bot Father이 메세지로 준 token)
		- Id를 확인하기 위한 URL
		- Id 확인
		- 보낼 message
		- message를 보낼 API(Telegram manual에서 확인)
### 2.2 Telegram & PythonAnywhere
- 구성요소: Naver API / 내 컴퓨터(Client)  / Telegram

- 작동방식
	- 1. Naver API에 최저가 정보를 request하면 알아서 respond
	- 2. respond받은 정보를 다듬어서 Telegram Server에 request
	- 3. request받은 정보를 print 함수로 표기
	- 필요한 것
		- 2.1 필요한 것
		- Naver에 접근하기 위한 key(Client_ID, Client_secret)
		- Naver URL
		- 받아온 정보를 저장할 장소(response)
	
-  PythonAnywhere

  Tasks에서 아래의 이미지와 같이 설정하면 자동 실행(영국시간기준)

  ![PythonAnywhere](02_1st_week_summary.assets/PythonAnywhere.png)
## 3. GitLab
- 자세한 설명은 00_markdown_basic.md에 있습니다
- 작동 순서
```
git init -> 

계정 메일 및 이름 생성
git config --global user.name ->  git config --global user.name 'fromecha' -> get config --global user.email -> git config --global user.email 'fromecha@gmail.com' -> git config --global user.email -> 

add & commit
git add README.md ->  git commit -m 'First Commit' ->  git log ->  git add homework/0118.md ->  git commit -m 'add 0118.md' -> git log ->  git status -> git add . -> git commit -m 'little change'
```


## 4. Which API did I used?
- [무작위 나이 생성기](https://api.agify.io/?name=mecha)
- [미세먼지](https://www.data.go.kr/index.do)
- [날씨 예보](https://www.metaweather.com/api/)
- [텔레그램 봇](https://core.telegram.org/bots/api)
- [네이버 개발자](https://developers.naver.com/main/)
- [프로그램 자동 실행기](https://www.pythonanywhere.com/user/chan/)


## 5. Utilization
- 미세먼지 & 날씨 에보를 모듈로 제작해 from ~ import로 사용 가능
-  









