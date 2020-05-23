# neispy

[![GitHub license](https://img.shields.io/github/license/SaidBySolo/neispy)](https://github.com/SaidBySolo/neispy/blob/master/LICENSE)
![Python package](https://github.com/SaidBySolo/neispy/workflows/Python%20package/badge.svg)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/26f53a7e434c4f079415ab23cb51700d)](https://app.codacy.com/manual/SaidBySolo/neispy/dashboard)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/neispy)](https://pypi.org/project/neispy/)

[Discord.py](https://github.com/Rapptz/discord.py)와 충돌이 발생하지 않게 aiohttp로 래핑하였습니다.

api키는 [이곳](https://open.neis.go.kr/portal/guide/actKeyPage.do)에서 받으실 수 있습니다.    

## 현재 사용가능한 종류

* 학교정보

* 학원및교습소정보

* 학사일정정보

* 급식정보

* 초,중,고 시간표정보

## 설치 방법

```sh
pip install neispy
```

## 업데이트 방법

```sh
pip install --upgrade neispy
```

## 사용 예시

```py
import neispy
import asyncio

name = "인천석천초등학교"


async def main():

    # 필수인자가 들어가는곳입니다. API키,json,xml등 받을방식등등..
    # 아무값이 없으니 샘플키로 요청합니다.
    neis = neispy.Client()

    # 학교이름으로 학교정보를 요청하고 교육청코드 와 학교코드로 가져옵니다.
    scinfo = await neis.schoolInfo(SCHUL_NM=name)
    AE = scinfo.ATPT_OFCDC_SC_CODE  # 교육청코드
    SE = scinfo.SD_SCHUL_CODE  # 학교코드

    # 학교코드와 교육청 코드로 2019년 1월 22일의 급식 정보 요청
    scmeal = await neis.mealServiceDietInfo(AE, SE, MLSV_YMD=20190122)
    meal = scmeal.DDISH_NM.replace('<br/>', '\n')# 줄바꿈으로 만든뒤 출력

    # 학교코드와 교육청 코드로 2019년 3월 7일날 학사일정 요청
    scschedule = await neis.SchoolSchedule(AE, SE, AA_YMD=20190307)
    schedule = scschedule.EVENT_NM #학사일정명 가져옴

    # 학교코드와 교육청 코드로 초등학교의 2020년 1월 22일의 시간표가져옴
    sctimetable = await neis.timeTable('els', AE, SE, 2019, 2, 20200122, 1, 1)
    timetable = [i['ITRT_CNTNT'] for i in sctimetable.data]# 리스트로 만듬

    academyinfo = await neis.acaInsTiInfo(AE) # 교육청 코드로 학원및 교습소 정보 요청
    academy = academyinfo.ACA_NM # 학교이름 출력

    scclass = await neis.classInfo(AE, SE, GRADE=1, rawdata=True)# 학교코드와 교육청 코드로 1학년의 모든 반정보 요청
    class_info = [i['CLASS_NM'] for i in scclass.data]# 리스트로만듬

    #출력
    print(AE)
    print(SE)
    print(meal)
    print(schedule)
    print(academy)
    print(class_info)
    print(timetable)

# 실행
loop = asyncio.get_event_loop()
loop.run_until_complete(main())

#출력값

#E10
#7341038
#보리밥
#사과
#비엔나소시지케첩조림2.5.6.10.12.13.
#궁중떡볶이1.5.6.13.
#알타리김치9.13.
#청국장찌개(신)5.9.13.
#학급임원선거
#A+수학교습소
#['1', '2', '3', '4', '5']
#['즐거운생활', '수학', '국어', '즐거운생활']
```

## 인자값

|변수명|타입|변수 설명|설명|
|---|-----|------|---------|
|KEY|STRING(필수)|인증키|기본값 : sample key|
|Type|STRING(필수)|호출 문서(xml, json)|기본값 : json|
|pIndex|INTEGER(필수)|페이지 위치|기본값 : 1(sample key는 1 고정)|
|pSize|INTEGER(필수)|페이지 당 신청 숫자|기본값 : 100(sample key는 5 고정)|

* [학교기본정보](https://open.neis.go.kr/portal/data/service/selectServicePage.do?page=1&rows=10&sortColumn=&sortDirection=&infId=OPEN17020190531110010104913&infSeq=2#2)

* [급식식단정보](https://open.neis.go.kr/portal/data/service/selectServicePage.do?page=1&rows=10&sortColumn=&sortDirection=&infId=OPEN17320190722180924242823&infSeq=2#2)

* [학사일정](https://open.neis.go.kr/portal/data/service/selectServicePage.do?page=1&rows=10&sortColumn=&sortDirection=&infId=OPEN17220190722175038389180&infSeq=2#2)

* [학원교습소정보](https://open.neis.go.kr/portal/data/service/selectServicePage.do?page=1&rows=10&sortColumn=&sortDirection=&infId=OPEN15920190423094641415608&infSeq=2)

* [시간표](https://open.neis.go.kr/portal/data/service/selectServicePage.do?page=1&rows=10&sortColumn=&sortDirection=&infId=OPEN15020190408160341416743&infSeq=2)

**시간표 같은 부분은 초,중,고인걸 제외하고는 모두 같으니 출력 항목만 보시면됩니다.**

## Patch note

### 0.6.0

* 모델 적용완료

* 반정보 엔드포인트 커버 완료

* 모든 정보가 필요할때 rawdata를 이용하여 리스트로 가져올수있습니다.

### 0.5.0

* Model 메커니즘 변경

* docstring 추가

### 0.4.0

* 초,중,고 시간표엔드포인트 커버가능

### 0.3.4

* Model 메커니즘 변경

### 0.3.3

* Model클래스에서 sort_meal함수의 이름이달라 생긴문제 수정

### 0.3.2

* 코드 퀄리티 향상

### 0.3.1

* 코드 퀄리티 향상

### 0.3.0

* **코드 다시 쓰기 분기 합병**
* 학원교습소 정보 추가
* 예외처리 추가
* 코드 최적화

### 0.2.3

* 초등학생 시간표 추가

### 0.2.2

* Issue #1 버그수정
* 샘플키로 요청하도록 변경

### 0.2.1

* 학사일정 추가

### 0.2.0

* 학교정보,급식일정 모든 인자값 받을수있음.

### 0.1.1

* 사용하지 않는 모듈 제거,사용하기쉽도록 함수이름 변경

### 0.1.0

* 첫 배포 시작
