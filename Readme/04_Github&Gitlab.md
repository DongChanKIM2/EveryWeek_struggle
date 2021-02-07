

# Github & lab

## 1. What is the Github & lab

- Git '분산형 버젼관리' + '원격 저장소'
- 프로젝트를 만들때마다 생기는 clone https:주소가 원격 저장소 역할을 해줌
- Issue tracking이 가능하므로 변경사항 추적 및 각자에게 업무 배분 및 파악 관리
- Github에 비해 보안 및 개별 프로젝트 진행하기에 용이함

## 2. 용어 정리
- server => github & lab / local computer => 내 노트북

## 3. local에서 git에 업로드할때(push)
1. 자기소개(내 이메일과 내 이름 등록) -> 내가 올렸다는 걸 모두가 알기 위해서 
git global setup: 
```
git config --global user.name "fromecha"
git config --global user.email "fromecha@gmail.com"
```
2. local computer에서 업로드하고 싶은 폴더 경로 설정

```
mkdir testproject
cd testproject
```

3. 폴더(testproject)를 git의 관리아래로 두겠다 라고 선언

```
git init #
# 원래 master이지만 인종차별 논란으로 인해 main으로 변경...
```

4. 폴더와 깃랩 연동시켜 깃랩의 저장소를 원격 저장소로 추가하는 작업

```
git remote add origin https://~~~
# https는 gitlab에서 만든 파일을 저장하고 싶은 주소
```

5. 폴더 내에서 코드 작성 및 파일 준비
```
touch README.md => 설명서
touch .gitignore => 올리고 싶지 않은 파일들
```
6. gitlab에 파일 업로드(파일 경로 및 깃랩 저장소 위치 주의할 것!)

```
git add . (전체 분장실로 보내기)
git commit -m '명령어' (분장 끝내고 stage로 가기)
git push -u origin master (stage위에서 사진찍기)
```



## 4. git에서 local로 데이터 다운받기
1. Git의 주소 입력
```
git clone https://gitlab주소 
# local computer에 데이터가 없을 때 원격 저장소의 데이터 가져오기
```

2. 내 local computer 주소로 이동

```
cd
cd 내 local computer 저장할 주소
```

3. Git에다가 내가 다운받았다는 기록 남기기

```
git pull 
# local computer에 데이터는 이미 있고 원격저장소에 기록 남기기
```

## 5. Github로 협업하기

### 5.1 협업 procedure
0. 매우 불행하게도 동시에 push 했을 때
	0.1. 조금 늦게 push한 사람은 error 발생, git pull, 내용 수정 후 git push origin main
	0.2. 이래서 branch가 협업할 때 중요하다

1. main 생성 후 branch 생성
```
# branch 생성
git branch __branch_name__
# branch인지 확인
git branch
```
2. main 에서 branch로 전환

```
git switch __branch_name__
```

extra 2. 1번, 2번 동시 수행
```
git switch -c __branch_name__
```

3. branch에서 add . & commit
```
git add .
git commit -m 'branch'
```

4. branch 에서 main 으로 전환
```
# branch 삭제 및 전환
git switch master
# 전환됬는지 확인
git log(head -> '현재 위치')
```
5. 병합
```
git merge __branch_name__
```

6. 기록 및 상황 보기
```
# 관리되고 있는 파일과 변경 사항 확인
git status
```
### 5.2 병합 종류

1. 꽃길만 걷자. FastForward
	
	- 새로운 걸 만드는게 아니라 branch 그대로 
	
2. 일반적인 Merge
3. 2번에서 merge 실패했을 때

	- automatic merge failed (master|merging)
	- 수정하고 다시 merge 시도

## 6. 깃허브와 서버
- 개요
  - 우리가 항상 컴퓨터를 켜놓고 정보를 줄 수 없기에 정보를 주기만 하는 역할의 서버가 필요함
  - GitHub Portfolio 페이지 또한 동일한 원리
- 깃허브 서버 관련된 사전 지식
  - ssh: 깃허브 서버가서 직접 수정하는 것 
- 서버에 접속해서 작업하려면? VIM 이 필요해
	- 서버에는 운영체제가 없으므로 vim이라는 유닉스로 파일 관리
- VIM 사용법
	- 작업하고 싶은 파일에서 git bash 로 vim으로 파일 열고 수정
    - vim Filename.html-> i(insert mode) -> 수정 -> esc탈출 -> 종료  ':q' / 저장: '':w" :wq 저장후 종료
	- git add 후에 git commit 하면 vim 들어가짐 commit msg 입력후 종료
