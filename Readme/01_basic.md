# Basic CLI(Command Line Interface)

## 0. Typora(MarkDown)에 대해서
- MarkUp(표시하다) -> Html(HyperText Markup Language) -> MarkDown
- Html에서 표시란 역할에 관한 것
  - 큰 제목<h1>~</h1> / 소제목<h2>~</h2> / 본문<h3>~</h3>
- MarkDown은 h1같은 역할 표시를 간소화시켜 #으로 구조화 가능

## 1. 폴더(directory) 관련 기호

폴더 상징 특수기호 

- `~`
  
  - Home 폴더를 의미(Home 폴더: 바탕화면 상위 폴더)
  - 위치는 일반적으로 /C/Users/[계정명]
  - cd~ 하면 Home폴더로 경로변경
  
- `/`
  
  - Root 폴더로 최상단을 의미
  
- `.`

  - 현재 위치

- `..`
- 상위 폴더 위치
  

## 2. Git
### 2.1 Git Bash 명령어

- `cd [대상폴더]`: 경로변경

- `ls`: 있는 목록 나열

- `rm`: 파일 제거

  - `rm *`: 모든 파일 제거(유의할 것!)

- `r`: 폴더 제거

- `mkdir`: 폴더/디렉토리 생성

- `touch`: 파일 생성

- `tab`: 자동완성

  ```
  $ mkdir TIL 
  $ cd TIL
  $ mkdir CLI
  $ cd CLI
  $ touch 01_basic.md  
  ```
### 2.2 Git vs Gitlab vs Github
- `git`: 사진첩(변경사항추적 및 이전자료 사용가능)
- `gitlab`: 숙제 및 실습 비공개용
- `github`: 클라우드 및 포트폴리오용

## 3. 월말평가
- vscode로 실행
- vscode Terminal On/Off 단축키: Ctrl + `

## 4. API
- 내가 필요한 정보를 Interface 할 수 있는 도구

## 4. 유용한 사이트
- [그림/PPT](https://www.autodraw.com)
- [AI게임](https://teachablemachine.withgoogle.com)
- https://www.metaweather.com/
- pip(pypi): 파이썬 라이브러리 메뉴얼

## 5. 중요 TIP
- 개발할 때 내부(라이브러리, 구조)를 뜯어보면서 이해하자
- EX)requests 모듈도 ctrl 누르고 내부를 보면 코드가 적혀있어

## 6. etc
- . 이나 () 붙어있으면 메서드
- 요청은 url로 보내면 응답이 온다
- 내가 요청을 보내면 requests, 응답은 response
- 요청 보내는 방법은 딱 한가지로 URL 이다
- 요청 없는 응답은 없다

- 봇 작동순서: 
- 1. Telegram bot 
- 2. python에서 telegram으로 요청 보내기 Web + Http
- 3. Telegram에서 vscode로 message response

- 필요한 데이터:
- 1. my_bot
- 2. '나'에 대한 데이터
- 3. message
- 4. URL


