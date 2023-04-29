# neispy

> [2020 공개SW 개발자 대회 조직위원장 특별상 수상 작품](https://www.oss.kr/dev_competition_activities/show/d8ce674e-1cf4-45de-b3c2-0365cdc5aabc?page=3)  
> **동기와 비동기 전부 지원합니다.** **문제 발생시 이슈 넣어주세요!**

[![GitHub license](https://img.shields.io/github/license/SaidBySolo/neispy)](https://github.com/SaidBySolo/neispy/blob/master/LICENSE)
![Python package](https://github.com/SaidBySolo/neispy/workflows/Python%20package/badge.svg)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/neispy)](https://pypi.org/project/neispy/)

api키는 [이곳](https://open.neis.go.kr/portal/guide/actKeyPage.do)에서 받으실 수 있습니다.

[open Neis api](https://open.neis.go.kr/)의 모든 엔드포인트가 래핑되어 있습니다.


```sh
pip install neispy
```

## 업데이트 방법

```sh
pip install --upgrade neispy
```

## 비슷한 프로젝트

* [neis.kt](https://github.com/kimcore/neis.kt)
  * OPEN NEIS API를 코틀린으로 래핑한 라이브러리입니다.
* [neis.ts](https://github.com/star0202/neis.ts)
  * TypeScript로 만들어진 NEIS Open API Wrapper

## 사용 예시(비동기)

```py
from neispy import Neispy
from asyncio.events import get_event_loop


name = "인천석천초등학교"


async def main():
    # 필수 인자가 들어가는 곳입니다. API키, JSON, XML 등의 받을 방식 등등..
    # 아무런 값이 없으니 샘플 키로 요청합니다.
    async with Neispy() as neis:
        # 학교 이름으로 학교 정보를 요청하고 교육청 코드와 학교 코드로 가져옵니다.
        scinfo = await neis.schoolInfo(SCHUL_NM=name)
        AE = scinfo[0].ATPT_OFCDC_SC_CODE  # 교육청 코드
        SE = scinfo[0].SD_SCHUL_CODE  # 학교 코드

        # 학교 코드와 교육청 코드로 2022년 5월 23일의 급식 정보 요청
        scmeal = await neis.mealServiceDietInfo(AE, SE, MLSV_YMD="20220523")
        meal = scmeal[0].DDISH_NM.replace("<br/>", "\n")  # 줄바꿈으로 만든 뒤 출력

        # 학교 코드와 교육청 코드로 2022년 6월 1일날 학사일정 요청
        scschedule = await neis.SchoolSchedule(AE, SE, AA_YMD=20220601)
        schedule = scschedule[0].EVENT_NM  # 학사일정명 가져옴

        # 학교 코드와 교육청 코드로 초등학교의 2022년 5월 23일의 시간표 가져옴
        sctimetable = await neis.elsTimetable(AE, SE, 2022, 1, 20220523, "1", "1")
        timetable = [i.ITRT_CNTNT for i in sctimetable]  # 리스트로 만듦

        academyinfo = await neis.acaInsTiInfo(AE)  # 교육청 코드로 학원 및 교습소 정보 요청
        academy = academyinfo[0].ACA_NM  # 학교 이름 출력

        scclass = await neis.classInfo(
            AE, SE, GRADE="1"
        )  # 학교 코드와 교육청 코드로 1학년의 모든 반 정보 요청
        class_info = [i.CLASS_NM for i in scclass]  # 리스트로 만듦

        hiscinfo = await neis.schoolInfo(SCHUL_NM="인천기계")  # 다른 정보를 위해 공고로 가져옴
        hAE = hiscinfo[0].ATPT_OFCDC_SC_CODE  # 교육청 코드
        hSE = hiscinfo[0].SD_SCHUL_CODE  # 학교 코드

        scmajorinfo = await neis.schoolMajorinfo(hAE, hSE)  # 학과 정보 요청
        majorinfo = [m.DDDEP_NM for m in scmajorinfo]  # 리스트로 만듦

        scAflcoinfo = await neis.schulAflcoinfo(hAE, hSE)  # 학교 계열 정보 요청
        Aflco = [a.ORD_SC_NM for a in scAflcoinfo]

        sctiClrm = await neis.tiClrminfo(hAE, hSE)  # 시간표 강의실 정보 요청
        tiClem = [t.CLRM_NM for t in sctiClrm]


get_event_loop().run_until_complete(main())

# 출력값

# E10
# 7341025
# 보리밥c  
# 감자국c  (5.6.9.13.)
# 순대볶음c  (5.6.10.13.)
# 고구마돈가스c  (1.2.5.6.10.12.13.)
# 배추김치  (9.13.)
# 참외  
# 지방선거일
# A+수학교습소
# ['1', '2', '3', '4', '1']
# ['국어', '수학', '즐거운생활', '즐거운생활', '봉사활동']
# ['공동실습소', '건축과', '건축디자인과', '금속과', '기계공작과']
# ['공동실습소', '공업계', '공업계']
# ['건축1-1', '건축1-2', '도시1-1', '도시1-2', '메카1-1']

```

## 사용 예시(동기)

```py
from neispy import Neispy

name = "인천석천초등학교"


def main():

    # 필수 인자가 들어가는 곳입니다. API키, JSON ,XML 등의 받을 방식 등등..
    # 아무런 값이 없으니 샘플 키로 요청합니다.
    neis = Neispy.sync()

    # 학교 이름으로 학교 정보를 요청하고 교육청 코드 와 학교 코드로 가져옵니다.
    scinfo = neis.schoolInfo(SCHUL_NM="인천동방초등학교")
    AE = scinfo[0].ATPT_OFCDC_SC_CODE  # 교육청 코드
    SE = scinfo[0].SD_SCHUL_CODE  # 학교 코드

    # 학교 코드와 교육청 코드로 2022년 5월 23일의 급식 정보 요청
    scmeal = neis.mealServiceDietInfo(AE, SE, MLSV_YMD="20220523")
    meal = scmeal[0].DDISH_NM.replace("<br/>", "\n")  # 줄바꿈으로 만든 뒤 출력

    # 학교 코드와 교육청 코드로 2022년 6월 1일날 학사일정 요청
    scschedule = neis.SchoolSchedule(AE, SE, AA_YMD=20220601)
    schedule = scschedule[0].EVENT_NM  # 학사일정명 가져옴

    # 학교 코드와 교육청 코드로 초등학교의 2022년 5월 23일의 시간표가져옴
    sctimetable = neis.elsTimetable(AE, SE, 2022, 1, 20220523, "1", "1")
    timetable = [i.ITRT_CNTNT for i in sctimetable]  # 리스트로 만듦

    academyinfo = neis.acaInsTiInfo(AE)  # 교육청 코드로 학원및 교습소 정보 요청
    academy = academyinfo[0].ACA_NM  # 학교이름 출력

    scclass = neis.classInfo(AE, SE, GRADE="1")  # 학교 코드와 교육청 코드로 1학년의 모든 반 정보 요청
    class_info = [i.CLASS_NM for i in scclass]  # 리스트로 만듦

    hiscinfo = neis.schoolInfo(SCHUL_NM="인천기계")  # 다른 정보를 위해 공고로 가져옴
    hAE = hiscinfo[0].ATPT_OFCDC_SC_CODE  # 교육청 코드
    hSE = hiscinfo[0].SD_SCHUL_CODE  # 학교 코드

    scmajorinfo = neis.schoolMajorinfo(hAE, hSE)  # 학과 정보 요청
    majorinfo = [m.DDDEP_NM for m in scmajorinfo]  # 리스트로 만듦

    scAflcoinfo = neis.schulAflcoinfo(hAE, hSE)  # 학교 계열 정보 요청
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

# 출력값

# E10
# 7341025
# 보리밥c  
# 감자국c  (5.6.9.13.)
# 순대볶음c  (5.6.10.13.)
# 고구마돈가스c  (1.2.5.6.10.12.13.)
# 배추김치  (9.13.)
# 참외  
# 지방선거일
# A+수학교습소
# ['1', '2', '3', '4', '1']
# ['국어', '수학', '즐거운생활', '즐거운생활', '봉사활동']
# ['공동실습소', '건축과', '건축디자인과', '금속과', '기계공작과']
# ['공동실습소', '공업계', '공업계']
# ['건축1-1', '건축1-2', '도시1-1', '도시1-2', '메카1-1']
```

## 인자값

| 변수명 | 타입          | 변수 설명            | 설명                              |
| ------ | ------------- | -------------------- | --------------------------------- |
| KEY    | STRING(필수)  | 인증키               | 기본값 : sample key               |
| Type   | STRING(필수)  | 호출 문서(xml, json) | 기본값 : json                     |
| pIndex | INTEGER(필수) | 페이지 위치          | 기본값 : 1(sample key는 1 고정)   |
| pSize  | INTEGER(필수) | 페이지 당 신청 숫자  | 기본값 : 100(sample key는 5 고정) |

* [데이터셋](https://open.neis.go.kr/portal/data/dataset/searchDatasetPage.do)

**시간표 같은 부분은 초, 중, 고, 특수인 것을 제외하고는 모두 같습니다.**

**Attribute도 데이터셋을 참고해 주시기 바랍니다.**

## Release note

### 4.0.0

* 클래스명 변경 ``Client`` -> ``Neispy``.
* 이제 ``ClientSession``을 요청마다 생성하지 않습니다.
* ``now()``함수가 더 이상 적용되지 않도록 변경되었습니다.
* ``async with`` 구문을 지원하도록 변경되었습니다.
* 기존 모델에서 SimpleNamespace로 변경되었습니다.
* 동기로 사용할시 클래스메소드 ``.sync()``의 반환값인 ``SyncNeispy``를 사용해야 하도록 변경되었습니다.
* 타입힌트가 좀 더 정확히 적용되었습니다.

### 3.2.2

* 사용하지 않는 모듈을 제거한 후 재배포했습니다.

### 3.2.1

* #43(#42번 이슈) PR을 적용했습니다.

### 3.2.0

* #41 PR을 적용했습니다.

### 3.1.0

* #40(#39번 이슈) PR을 적용했습니다.

### 3.0.0

* #28(#17번 이슈) #31(#30번 이슈) #34(#33번 이슈) #36 PR을 적용했습니다.

* 동기 비동기 클라이언트를 나누지 않고 사용할수있습니다.

* 모델의 많은 변화가 있습니다. 예제를 참고해주세요.

### 2.0.7

* neispy는 이제 UTC+9:00를 기준으로 가져옵니다.

### 2.0.6

* #25번 이슈를 적용했습니다.

* APIKeyNotFound예외를 force인자를 통해 무시할 수 있습니다.

* 시간표에 빠져있던 강의실명 파라미터를 추가했습니다.

### 2.0.4

* #22번(#21번 이슈), #23번 PR을 적용했습니다.

### 2.0.3

* #20번 PR을 적용했습니다.

### 2.0.2

* Fixed #15

* 시간표에 빠져있던 인자들을 추가했습니다.

### 2.0.1

* 날짜 형식이 20200101과 같은 형식으로 안나오는 문제를 해결했습니다.

### 2.0.0

* 동기 요청이 가능합니다.

### 1.0.0

* 모든 엔드포인트를 커버합니다.

### 0.6.0

* 모델을 적용했습니다.

* 반 정보 엔드포인트를 커버할 수 있습니다.

* 모든 정보가 필요할 때 rawdata를 이용하여 리스트로 가져올 수 있습니다.

### 0.5.0

* Model 메커니즘을 변경했습니다.

* docstring을 추가했습니다.

### 0.4.0

* 초, 중, 고 시간표 엔드포인트를 커버할 수 있습니다.

### 0.3.4

* Model 메커니즘을 변경하였습니다.

### 0.3.3

* Model 클래스에서 sort_meal 함수의 이름이 달라 생긴 문제를 수정했습니다.

### 0.3.2

* 코드 퀄리티가 향상되었습니다.

### 0.3.1

* 코드 퀄리티가 향상되었습니다.

### 0.3.0

* **코드 다시 쓰기 분기를 합병했습니다.**
* 학원교습소 정보를 추가했습니다.
* 예외 처리를 추가했습니다.
* 코드를 최적화했습니다.

### 0.2.3

* 초등학생 시간표를 추가했습니다.

### 0.2.2

* #1번 이슈의 버그를 수정했습니다.
* 샘플 키로 요청하도록 변경했습니다.

### 0.2.1

* 학사 일정을 추가했습니다.

### 0.2.0

* 학교 정보, 급식 일정 모든 인자 값을 받을 수 있습니다.

### 0.1.1

* 사용하지 않는 모듈을 제거하고, 사용하기 쉽도록 함수 이름을 변경했습니다.

### 0.1.0

* 첫 배포가 시작되었습니다.
