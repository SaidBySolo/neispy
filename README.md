# neispy

**현재 급식,학교 정보,학사 일정만 가져올수있습니다.**  

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/26f53a7e434c4f079415ab23cb51700d)](https://www.codacy.com/manual/SaidBySolo/neispy?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=SaidBySolo/neispy&amp;utm_campaign=Badge_Grade)
![PyPI - Downloads](https://img.shields.io/pypi/dm/neispy)

[Discord.py](https://github.com/Rapptz/discord.py)와 충돌이나지않게 aiohttp로 래핑하였습니다.

Api키는 [이곳](https://open.neis.go.kr/)여기서 받으실수있습니다.  

여러분의 스타는 제작자의 의욕입니다!

## 설치 방법

```sh
pip install neispy
```

## 업데이트 방법

```sh
pip install --upgrade neispy
```

## Example

```py
import asyncio
import json
from neispy import lunch, school, schedule, sort, eletime

#api키 없을시 샘플키로 요청함
#사용을 제대로하시려면 api키를 넣어주세요

name="인천석천초등학교"

async def main():
    #먼저 필수인자를 합칩니다. api키가없으면 샘플키로요청됩니다.
    param = await sort.sort_reqarg()

    #필수인자와 이름을 인자로넣어주면 요청(json,xml)값에따른 형식인 str로반환됩니다.
    scinfo = await school.schoolinfo(param, SCHUL_NM=name)
    #json형식을 넣어주면 시도교육청코드와,표준학교코드를 튜플형식으로 반환됩니다.
    AE, SE = await sort.sort_schoolcode(scinfo)

    #필수인자,시도교육청코드와,표준학교코드,급식일을 인자값으로 넣으면 요청(json,xml)값에따른 형식인 str로반환됩니다.
    lunchinfo = await lunch.lunchinfo(param, AE, SE, MLSV_YMD=20190122)
    #json값을 정리하여 급식메뉴만 반환합니다.
    lunchmenu = await sort.sort_lunchmenu(lunchinfo)

    #AE,SE는 교육청, 학교코드입니다. 2019학년도 2학기 2020년01월22일 1학년1반의 시간표를 요청(json,xml)값에따른 형식인 str로반환됩니다.
    timetable = await eletime.timetable(param,AE,SE,2019,2,20200122,1,1)
    #json값을 정리해 시간표 순서대로 리스트로반환합니다.
    sorttimetable = await sort.sort_timetable(timetable)

    #20190307날의 학사일정을 요청(json,xml)값에따른 형식인 str로반환됩니다.
    schdate = await schedule.schoolshd(param,AE,SE,AA_YMD=20190307)
    #json값을 정리해 학사일정명만 반환합니다.
    sortschdate = await sort.sort_scdname(schdate)

    print(lunchmenu)
    print(sorttimetable)
    print(sortschdate)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())

#출력
보리밥
사과
비엔나소시지케첩조림2.5.6.10.12.13.
궁중떡볶이1.5.6.13.
알타리김치9.13.
청국장찌개(신)5.9.13.
['즐거운생활', '수학', '국어', '즐거운생활']
학급임원선거
```

## 인자값

|변수명|타입|변수 설명|설명|
|---|-----|------|---------|
|KEY|STRING(필수)|인증키|기본값 : sample key|
|Type|STRING(필수)|호출 문서(xml, json)|기본값 : json|
|pIndex|INTEGER(필수)|페이지 위치|기본값 : 1(sample key는 1 고정)|
|pSize|INTEGER(필수)|페이지 당 신청 숫자|기본값 : 100(sample key는 5 고정)|

## Patch note

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
