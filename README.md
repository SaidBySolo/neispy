# neispy

**현재 급식,학교 정보,학사 일정만 가져올수있습니다.**  

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/26f53a7e434c4f079415ab23cb51700d)](https://www.codacy.com/manual/SaidBySolo/neispy?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=SaidBySolo/neispy&amp;utm_campaign=Badge_Grade)
![PyPI - Downloads](https://img.shields.io/pypi/dm/neispy)

[Discord.py](https://github.com/Rapptz/discord.py)와 쉽게 연동하여 사용하실수있습니다.

Api키는 [이곳](https://open.neis.go.kr/)여기서 받으실수있습니다.

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
from neispy import lunch, school, schedule, sort

#api키 없을시 샘플키로 요청함
#사용을 제대로하시려면 api를 넣어주세요

name="인천기계공업고등학교"

async def main():
    param = await sort.sort_reqarg(key)
    scinfo = await school.schoolinfo(param, SCHUL_NM=name)
    AE, SE = await sort.sort_schoolcode(scinfo)
    lunchinfo = await lunch.lunchinfo(param, AE, SE, MLSV_YMD=20190102)
    lunchmenu = await sort.sort_lunchmenu(lunchinfo)
    scd = await schedule.schoolshd(param, AE, SE, AA_YMD=20190408)
    eventname = await sort.sort_scdname(scd)
    print(eventname)
    print(lunchmenu)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

#실행 결과
지방기능경기대회
비빔밥(고)5.13.
계란북어국(고)1.5.6.13.
해시브라운/케찹(고)1.2.12.
배추김치(고)9.
볶음고추장(고)5.6.10.13.
삼색과일
```

## 인자값

|변수명|타입|변수 설명|설명|
|---|-----|------|---------|
|KEY|STRING(필수)|인증키|기본값 : sample key|
|Type|STRING(필수)|호출 문서(xml, json)|기본값 : json|
|pIndex|INTEGER(필수)|페이지 위치|기본값 : 1(sample key는 1 고정)|
|pSize|INTEGER(필수)|페이지 당 신청 숫자|기본값 : 100(sample key는 5 고정)|

## Patch note

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
