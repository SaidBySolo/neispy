# neispy

**현재 급식, 학교 정보, 학사 일정만 가져올수있습니다.**  

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/26f53a7e434c4f079415ab23cb51700d)](https://app.codacy.com/manual/SaidBySolo/neispy/dashboard)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/neispy)](https://pypi.org/project/neispy/)

[Discord.py](https://github.com/Rapptz/discord.py)와 충돌이 발생하지 않게 aiohttp로 래핑하였습니다.

api키는 [이곳](https://open.neis.go.kr/portal/guide/actKeyPage.do)에서 받으실 수 있습니다.    

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
import asyncio
import neispy

name="인천석천초등학교"

async def main():

    #필수인자가 들어가는곳입니다. API키,json,xml등 받을방식등등..
    #아무값이 없으니 샘플키로 요청합니다.
    neis = neispy.Client()

    #학교이름으로 학교정보를 요청하고 그 반환값을 정리하여 교육청코드와학교코드로 가져옵니다.
    scinfo = await neis.schoolInfo(SCHUL_NM=name)
    AE,SE = neispy.sort_code(scinfo)

    #학교코드로 20190122날의 급식정보를 요청하고 반환값을 정리하여 급식 항목만 가져옵니다.
    scmeal = await neis.mealServiceDietInfo(AE,SE,MLSV_YMD=20190122)
    mealinfo = neispy.sort_meal(scmeal)

    #학교코드로 20190307날의 학사일정을 요청하고 반환값을 정리하여 학사일정이름만 가져옵니다.
    scschedule = await neis.SchoolSchedule(AE,SE,AA_YMD=20190307)
    scheduleinfo = neispy.sort_schedule(scschedule)

    #학교코드로 20200122날의 시간표을 요청하고 반환값을 정리하여 시간표만 가져옵니다.
    sctimetable = await neis.elsTimetable(AE,SE,2019,2,20200122,1,1)
    timetableinfo = neispy.sort_elstimetable(sctimetable)

    #출력
    print(AE)
    print(SE)
    print(mealinfo)
    print(scheduleinfo)
    print(timetableinfo)
    

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

## 인자값

|변수명|타입|변수 설명|설명|
|---|-----|------|---------|
|KEY|STRING(필수)|인증키|기본값 : sample key|
|Type|STRING(필수)|호출 문서(xml, json)|기본값 : json|
|pIndex|INTEGER(필수)|페이지 위치|기본값 : 1(sample key는 1 고정)|
|pSize|INTEGER(필수)|페이지 당 신청 숫자|기본값 : 100(sample key는 5 고정)|

## Patch note

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
