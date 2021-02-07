
# Web(Html&Css)
## 1. Web이란?
- w3c가 HTML5 표준이면 WHATWG(Google, MS..)로 승기가 넘어옴
- HTML(Hyper Text Markup Language)
	+ Hyper: 기존의 txt처럼 page가 아니라 다중으로 연결됨
	+ markup: 구조화됨 ex)대주제, 소주제 분류 
- 파이썬은 공식문서 PEF8, Stackoverflow를 보듯이 웹은 MDN 웹문서가 교과서 EX) html a tag mdn

## 2. HTML의 인터페이스 DOM
- DOM Tree(Document Object Model): 웹 페이지의 인터페이스로 유효한 HTML 문서의 인터페이스
	+ DOM은 Html문서가 객체 기반 표현으로 이루어진것을 일컬음
	+ DOM의 장점으로는 언어가 달라도 사용가능한 것 ex) body, h1
	+ 구조화된 문서
- HTML 특성
	+ Semantic tag(h1, table, strong, em) VS Nonsemantic tag(div, span, b, i)
		- Semantic tag 사용 이유
		1. 주제별로(대주제, 소주제) 브라우징에 같이 출력
		2. 시각장애인들 사용에 편리
	+ Block(h1, head) VS inline(span, a, form-input)
	+ 끊임없는 발전	
		
		- og(open graph protocol): 카톡에서 링크 보내면 생기는 미리보기 이미지(Facebook개발)
	+ https://www.youtube.com/watch?v=PizkhskZrKk 날잡고 함 봅시다!
## 3. 단축키
- 기본 구조: ! + Tab
- 끝 줄 엔터: Ctrl + 엔터
- 윗 줄 엔터: Ctrl + shift + 엔터
- 줄 자체 이동: Alt + 위아래 
- Chrome 실행: Alt + b
- VsCode 줄맞춤 자동서식: shift + alt + F
- List 구조:  ul>li*3
```
<ul>(unorderd list)
  <li> </li>
  <li> </li>
  <li> </li>  
</ul>
```

## 4. HTML Tag
- head: 웹 페이지 정보 및 외부 파일 링크할 때 사용
	
	+ title, meta등이 들어감
- meta: 문자 인코딩 및 키워드 
	
	+ <meta charset = "utf-8">
- div: 의미 없고 컨텐츠들을 어떤 목적에 따라 묶을 때 사용(block element)
- span: div와 동일 but inline element
- a: 웹 페이지나 외부 사이트 연결
	+ 속성 값:
  
  ```
  _blank: 새로운 창 열기
  _self: 현재 창
  ```
- link: 외부 파일 연결 ex)css
- img: 이미지 삽입 ex) <img src='이미지경로'>
	+ 이미지 경로
		- 1. 직접경로
		- 2. 간접경로
		- 3. 웹 검색 경로 
- p(pargraph): 내용 앞뒤로 빈 줄이 생기며 단락 생성
- ol~li
```
<ol>(ordered list)
  <li> 본문 </li>
  <li> 본문 </li>
</ol>
```
- ul~li
```
순서 없는 것(ul, li)
단축키 : ul>li*3
<ul>(unorderd list)
  <li> </li>
  <li> </li>
  <li> </li>  
</ul>
```
- br: 줄 바꿈
- h1~h6: 제목
- form: form의 요소(input..)이 여러 개일때 ul을 이용해 묶어줌
- input: form의 요소 중 하나로 사용자가 정보를 입력할 때 필요
- button: form의 요소 중 하나
- nav: 문서 연결 링크
- strong: 중요 내용 강조(b보다 용이 especially 시각장애인)
- footer: 제작 정보와 저작권
- header: 제목 지정
	+ head는 title로 한 번만 사용하고 header는 여러 번 사용
- Semantic Tag의 대표적인 구조:
	+ header: 제목, 로고
	+ content: 내용
	+ side bar: 본문 외 내용
	+ footer: 저작권

## 5. Block VS Inline(CSS Display)
- Block:
	+ 한 줄에 하나씩
	+ 가로와 세로 길이를 가짐
	+ 화면 배치를 위해 사용
	+ Inline 요소로 변경 가능(display: inline)
	+ Block 내부에 Block이나 Inline 삽입가능
	  + Inline-block
	+ Block요소 내부의 Text는 따로 align 처리을 해야함
	+ 태그: div, article, aside, footer, h1~6, ol, ul, table, section
- Inline:
	+ 한 줄에 여러 요소
	+ 가로 세로 길이는 없지만 내용물의 크기만큼 가짐
	+ 텍스트를 꾸밀 때 사용
	+ Inline 내부에 Inline은 가능하지만 Block은 불가능
	+ 태그: a, b, em, i, img, input, label, select, span, strong

## 6. CSS(Cascading style sheet)

+ CSS를 Html에 적용하는 3가지
	1. 인라인
	해당 태그에 직접 style 속성 활용
	2. 내부참조
	head 태그 내에 <style>지정
	3. 외부참조(내부참조보다 중복 지양)
	head에 link 활용

- css 우선순위
  + !importane > 인라인(줄 내부에서) > id 선택자 > class 선택자>요소 선택자>소스코드 아래가 마지막 실행
  + class 선택자 사용을 최고 권장

- 상속
  되는 것: text관련(font, color, text-align), opacity, visibility
  안되는것: position 관련요소(top, left, ritgh, bottom)

- 상대크기
	+ em: 배수 단위 / 요소에 지정된 사이즈의 상대적인 사이즈
	+ rem: 최상위 요소(html) 사이즈를 기준으로 배수 단위(1rem: 16px)

- 색상:
	1. 색상 키워드 black, white
	2. RGB색상 #000, #000000 OR rgb(0, 0, 0)
	3. HSL 색상,채도,명도	

- BOX model
	+ 모든 요소는 네모이고 동그라미도 네모를 깎아서 만든 것!
	+ margin>border>padding>content
	+ 테두리바깥여백>테두리영역>테두리안쪽내부>글이나 이미지 내용

- selector
	+ class: .
		- css는 class로 구조를 짜고 적용하는게 best
	+ id: #
		- id는 자바스크립트에서 사용
- Position
	+ static: 기본으로 top, bottom, left, right 속성값 적용불가
	+ relative: 
		- 태그의 위치를 변경하고 싶을 때 static 기준으로 계산
		- top, bottom, left, right 속성값 적용가능
		- 양보 안하는 욕심쟁이(팝업) / 부모
	+ absolute:
		- relative와 달리 원래 위치와 상관없이 위치 지정 가능
		- static 제외한 가장 가까운 상위 요소를 기준으로 함
		- 상위요소가 없으면 html 기준
		- 바깥쪽에 공간 생기지 않음
		- 양보하는 큰형 / 자식
	+ fixed:
		- 브라우저 화면의 상대 위치
- 자손선택자 VS 자식선택자
	+ 자손 선택자: 특정 요소의 자손으로 자식, 손자 등 후손 포함
	  + div 띄어쓰기 p
	+ 자식 선택자: 특정 요소의 자식만 선택
	  + div > p
	  + div > p:nth-child(){}: 전체
	  + div > p:nth-of-type(){}: 해당 class만
	


- Float
	- 원래는 이미지 주변으로 텍스트를 둘러사는 레이아웃을 위해 도입	
	- 이미지가 아닌 요소에도 적용해 웹사이트의 전체 레이아웃에도 적용(네이버 nav)
	- 속성: none 없음 / left 요소를 왼쪽으로 띄움 / right 오른쪽으로 요소 띄움
	- float한계로 flexbox 등장!두두두

- Flexbox
	- 단방향 레이아웃
	- 축(main axis~corss axis)
	- 요소(container~item)
```
사용 방법:
대부분: 부모 class에 display: flex; 지정
	가로: jusitfy-content
	세로: align-items(줄), align-self(개별)
	세로: align-content(전체)
	방향 설정: flex-direction: 바라보는 시점이 바뀌므로 start, end도 반대
	- column으로 바꾸면 justify-content가 세로, align-items가 가로로 바뀜
	한줄~여러줄 정렬: flex-wrap
	flew-flow: flex-wrap + flex-direction 
개별지정:
	우선순위: order -1 / 기본값: 0 / 1
	align-self: 요소 align-items와 동일

```
- Bootstrap의 Grid system 이용한 responsive web 

  + one source multi use
  + bootstrap_reboot -> 웹 css 초기화 (bootstrap css에 포함되잇음)
    - reset: 추천x 너무 다 날라감
    - normalize: 추천!!

  - CDN: 외부 서버를 사용해 부트스트랩 부담 다운(한번실행하면 캐시 생김)

자바스크립트가 뭐냐??



combination: + 는 바로 뒤만 ~는 뒤 전부



ssh: 서버가서 직접 수정하는 거 

해당위치가고 html 파일 열기: vim index.html-> i(insert mode) -> 수정 -> esc탈출 -> 종료  ':q' / 저장: '':w" :wq 저장후 종료

git add 후에 git commit 하면 vim 들어가짐 commit msg 입력후 종료

