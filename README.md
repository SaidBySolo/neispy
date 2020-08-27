# neispy

> **동기와 비동기 전부 지원합니다.** **문제 발생시 이슈 넣어주세요!**

[![GitHub license](https://img.shields.io/github/license/SaidBySolo/neispy)](https://github.com/SaidBySolo/neispy/blob/master/LICENSE)
![Python package](https://github.com/SaidBySolo/neispy/workflows/Python%20package/badge.svg)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/neispy)](https://pypi.org/project/neispy/)

기초적인 사용법은 [이곳](https://www.koreaminecraft.net/dev_portal/1790805)을 봐주세요!

api키는 [이곳](https://open.neis.go.kr/portal/guide/actKeyPage.do)에서 받으실 수 있습니다.

[open Neis api](https://open.neis.go.kr/)의 모든 엔드포인트가 래핑되어있습니다

```sh
pip install neispy
```

## 업데이트 방법

```sh
pip install --upgrade neispy
```

## 사용 예시(비동기)

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
    AE = scinfo[0].ATPT_OFCDC_SC_CODE  # 교육청코드
    SE = scinfo[0].SD_SCHUL_CODE  # 학교코드

    # 학교코드와 교육청 코드로 2019년 1월 22일의 급식 정보 요청
    scmeal = await neis.mealServiceDietInfo(AE, SE, MLSV_YMD=20190122)
    meal = scmeal[0].DDISH_NM.replace("<br/>", "\n")  # 줄바꿈으로 만든뒤 출력

    # 학교코드와 교육청 코드로 2019년 3월 7일날 학사일정 요청
    scschedule = await neis.SchoolSchedule(AE, SE, AA_YMD=20190307)
    schedule = scschedule[0].EVENT_NM  # 학사일정명 가져옴

    # 학교코드와 교육청 코드로 초등학교의 2020년 1월 22일의 시간표가져옴
    sctimetable = await neis.timeTable("els", AE, SE, 2019, 2, 20200122, 1, 1)
    timetable = [i.ITRT_CNTNT for i in sctimetable]  # 리스트로 만듬

    academyinfo = await neis.acaInsTiInfo(AE)  # 교육청 코드로 학원및 교습소 정보 요청
    academy = academyinfo[0].ACA_NM  # 학교이름 출력

    scclass = await neis.classInfo(AE, SE, GRADE=1)  # 학교코드와 교육청 코드로 1학년의 모든 반정보 요청
    class_info = [i.CLASS_NM for i in scclass]  # 리스트로만듬

    hiscinfo = await neis.schoolInfo(SCHUL_NM="인천기계")  # 다른정보를 위해 공고로 가져옴
    hAE = hiscinfo[0].ATPT_OFCDC_SC_CODE  # 교육청코드
    hSE = hiscinfo[0].SD_SCHUL_CODE  # 학교코드

    scmajorinfo = await neis.schoolMajorinfo(hAE, hSE)  # 학과정보 요청
    majorinfo = [m.DDDEP_NM for m in scmajorinfo]  # 리스트로 만듬

    scAflcoinfo = await neis.schulAflcoinfo(hAE, hSE)  # 학교 계열정보 요청
    Aflco = [a.ORD_SC_NM for a in scAflcoinfo]

    sctiClrm = await neis.tiClrminfo(hAE, hSE)  # 시간표 강의실 정보 요청
    tiClem = [t.CLRM_NM for t in sctiClrm]

    print(AE)
    print(SE)
    print(meal)
    print(schedule)
    print(academy)
    print(class_info)
    print(timetable)
    print(majorinfo)
    print(Aflco)
    print(tiClem)


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
#['기계과', '공동실습소', '건축과', '건축디자인과', '금속과']
#['공업계', '공동실습소', '공업계']
#['건축1-1', '건축1-2', '도시1-1', '도시1-2', '메카1-1']
```

## 사용 예시(동기)

```py
import neispy

name = "인천석천초등학교"


def main():

    # 필수인자가 들어가는곳입니다. API키,json,xml등 받을방식등등..
    # 아무값이 없으니 샘플키로 요청합니다.
    neis = neispy.Client()

    # 학교이름으로 학교정보를 요청하고 교육청코드 와 학교코드로 가져옵니다.
    scinfo = neis.schoolInfo(SCHUL_NM=name)
    AE = scinfo[0].ATPT_OFCDC_SC_CODE  # 교육청코드
    SE = scinfo[0].SD_SCHUL_CODE  # 학교코드

    # 학교코드와 교육청 코드로 2019년 1월 22일의 급식 정보 요청
    scmeal = neis.mealServiceDietInfo(AE, SE, MLSV_YMD=20190122)
    meal = scmeal[0].DDISH_NM.replace("<br/>", "\n")  # 줄바꿈으로 만든뒤 출력

    # 학교코드와 교육청 코드로 2019년 3월 7일날 학사일정 요청
    scschedule = neis.SchoolSchedule(AE, SE, AA_YMD=20190307)
    schedule = scschedule[0].EVENT_NM  # 학사일정명 가져옴

    # 학교코드와 교육청 코드로 초등학교의 2020년 1월 22일의 시간표가져옴
    sctimetable = neis.timeTable("els", AE, SE, 2019, 2, 20200122, 1, 1)
    timetable = [i.ITRT_CNTNT for i in sctimetable]  # 리스트로 만듬

    academyinfo = neis.acaInsTiInfo(AE)  # 교육청 코드로 학원및 교습소 정보 요청
    academy = academyinfo[0].ACA_NM  # 학교이름 출력

    scclass = neis.classInfo(AE, SE, GRADE=1)  # 학교코드와 교육청 코드로 1학년의 모든 반정보 요청
    class_info = [i.CLASS_NM for i in scclass]  # 리스트로만듬

    hiscinfo = neis.schoolInfo(SCHUL_NM="인천기계")  # 다른정보를 위해 공고로 가져옴
    hAE = hiscinfo[0].ATPT_OFCDC_SC_CODE  # 교육청코드
    hSE = hiscinfo[0].SD_SCHUL_CODE  # 학교코드

    scmajorinfo = neis.schoolMajorinfo(hAE, hSE)  # 학과정보 요청
    majorinfo = [m.DDDEP_NM for m in scmajorinfo]  # 리스트로 만듬

    scAflcoinfo = neis.schulAflcoinfo(hAE, hSE)  # 학교 계열정보 요청
    Aflco = [a.ORD_SC_NM for a in scAflcoinfo]

    sctiClrm = neis.tiClrminfo(hAE, hSE)  # 시간표 강의실 정보 요청
    tiClem = [t.CLRM_NM for t in sctiClrm]

    print(AE)
    print(SE)
    print(meal)
    print(schedule)
    print(academy)
    print(class_info)
    print(timetable)
    print(majorinfo)
    print(Aflco)
    print(tiClem)


main()

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
#['기계과', '공동실습소', '건축과', '건축디자인과', '금속과']
#['공업계', '공동실습소', '공업계']
#['건축1-1', '건축1-2', '도시1-1', '도시1-2', '메카1-1']
```

## 인자값

| 변수명 | 타입          | 변수 설명            | 설명                              |
| ------ | ------------- | -------------------- | --------------------------------- |
| KEY    | STRING(필수)  | 인증키               | 기본값 : sample key               |
| Type   | STRING(필수)  | 호출 문서(xml, json) | 기본값 : json                     |
| pIndex | INTEGER(필수) | 페이지 위치          | 기본값 : 1(sample key는 1 고정)   |
| pSize  | INTEGER(필수) | 페이지 당 신청 숫자  | 기본값 : 100(sample key는 5 고정) |

* [데이터셋](https://open.neis.go.kr/portal/data/dataset/searchDatasetPage.do)

**시간표 같은 부분은 초,중,고,특수인걸 제외하고는 모두 같습니다.**

**Attribute도 데이터셋을 참고해주시기바랍니다.**

## Patch note

### 3.0.0

* #28(#17번 이슈) #31(#30번 이슈) #34(#33번 이슈) #36 PR적용

* 동기 비동기 클라이언트를 나누지않고 사용할수있습니다.

* 모델의 많은변화가있습니다. 예제를 참고해주세요

### 2.0.7

* neispy는 이제 UTC+9:00를 기준으로 가져옵니다.

### 2.0.6

* #25번 이슈적용

* APIKeyNotFound예외를 force인자를 통해 무시할수있습니다.

* 시간표에 빠져있던 강의실명 파라미터를 추가했습니다.

### 2.0.4

* #22번(#21번 이슈), #23번 PR적용

### 2.0.3

* #20번 PR 적용

### 2.0.2

* Fixed #15

* 시간표에 빠져있던 인자들 추가

### 2.0.1

* 날짜형식이 20200101과 같은 형식으로 안나오는 문제 해결

### 2.0.0

* 동기 요청이 가능합니다.

### 1.0.0

* 모든 엔드포인트를 커버합니다.

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
