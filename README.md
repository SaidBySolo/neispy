# neispy

> [2020 공개SW 개발자 대회 조직위원장 특별상 수상 작품](https://www.oss.kr/dev_competition_activities/show/d8ce674e-1cf4-45de-b3c2-0365cdc5aabc?page=3)  
> **동기와 비동기 전부 지원합니다.** **문제 발생시 이슈 넣어주세요!**

[![GitHub license](https://img.shields.io/github/license/SaidBySolo/neispy)](https://github.com/SaidBySolo/neispy/blob/master/LICENSE)
![Python package](https://github.com/SaidBySolo/neispy/workflows/Python%20package/badge.svg)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/neispy)](https://pypi.org/project/neispy/)

api키는 [이곳](https://open.neis.go.kr/portal/guide/actKeyPage.do)에서 받으실 수 있습니다.

[open neis api](https://open.neis.go.kr/)의 모든 엔드포인트가 래핑되어 있습니다.

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

async def main():
    # 필수 인자가 들어가는 곳입니다. API키 등등..
    # 아무런 값이 없으니 샘플 키로 요청합니다.
    async with Neispy() as neis:
        # 학교 이름으로 학교 정보를 요청하고 교육청 코드 와 학교 코드로 가져옵니다.
        scinfo = await neis.schoolInfo(SCHUL_NM="인천동방초등학교")
        row = scinfo.schoolInfo[1].row[0]

        AE = row.ATPT_OFCDC_SC_CODE  # 교육청 코드
        SE = row.SD_SCHUL_CODE  # 학교 코드

        # 학교 코드와 교육청 코드로 2022년 5월 23일의 급식 정보 요청
        scmeal = await neis.mealServiceDietInfo(
            ATPT_OFCDC_SC_CODE=AE, SD_SCHUL_CODE=SE, MLSV_YMD="20220523"
        )
        row = scmeal.mealServiceDietInfo[1].row[0]
        meal = row.DDISH_NM.replace("<br/>", "\n")  # 줄바꿈으로 만든 뒤 출력

        # 학교 코드와 교육청 코드로 2022년 6월 1일날 학사일정 요청
        scschedule = await neis.SchoolSchedule(
            ATPT_OFCDC_SC_CODE=AE, SD_SCHUL_CODE=SE, AA_YMD=20220601
        )
        row = scschedule.SchoolSchedule[1].row[0]
        schedule = row.EVENT_NM  # 학사일정명 가져옴

        # 학교 코드와 교육청 코드로 초등학교의 2022년 5월 23일의 시간표가져옴
        sctimetable = await neis.elsTimetable(
            ATPT_OFCDC_SC_CODE=AE,
            SD_SCHUL_CODE=SE,
            AY="2022",
            SEM="1",
            ALL_TI_YMD=20220523,
            GRADE="1",
            PERIO=1,
        )
        timetable = [i.ITRT_CNTNT for i in sctimetable.elsTimetable[1].row]  # 리스트로 만듦

        academyinfo = await neis.acaInsTiInfo(
            ATPT_OFCDC_SC_CODE=AE
        )  # 교육청 코드로 학원및 교습소 정보 요청
        academy = academyinfo.acaInsTiInfo[1].row[0].ACA_NM  # 학교이름 출력

        scclass = await neis.classInfo(
            ATPT_OFCDC_SC_CODE=AE, SD_SCHUL_CODE=SE, GRADE="1"
        )  # 학교 코드와 교육청 코드로 1학년의 모든 반 정보 요청
        class_info = [i.CLASS_NM for i in scclass.classInfo[1].row]  # 리스트로 만듦

        hiscinfo = await neis.schoolInfo(SCHUL_NM="인천기계")  # 다른 정보를 위해 공고로 가져옴
        hirow = hiscinfo.schoolInfo[1].row[0]
        hAE = hirow.ATPT_OFCDC_SC_CODE  # 교육청 코드
        hSE = hirow.SD_SCHUL_CODE  # 학교 코드

        scmajorinfo = await neis.schoolMajorinfo(
            ATPT_OFCDC_SC_CODE=hAE, SD_SCHUL_CODE=hSE
        )  # 학과 정보 요청
        majorinfo = [m.DDDEP_NM for m in scmajorinfo.schoolMajorinfo[1].row]  # 리스트로 만듦

        scAflcoinfo = await neis.schulAflcoinfo(
            ATPT_OFCDC_SC_CODE=hAE, SD_SCHUL_CODE=hSE
        )  # 학교 계열 정보 요청
        Aflco = [a.ORD_SC_NM for a in scAflcoinfo.schulAflcoinfo[1].row]

        sctiClrm = await neis.tiClrminfo(
            ATPT_OFCDC_SC_CODE=hAE, SD_SCHUL_CODE=hSE
        )  # 시간표 강의실 정보 요청
        tiClem = [t.CLRM_NM for t in sctiClrm.tiClrminfo[1].row]
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


def main():
    # 필수 인자가 들어가는 곳입니다. API키 등등..
    # 아무런 값이 없으니 샘플 키로 요청합니다.
    neis = Neispy.sync()

    # 학교 이름으로 학교 정보를 요청하고 교육청 코드 와 학교 코드로 가져옵니다.
    scinfo = neis.schoolInfo(SCHUL_NM="인천동방초등학교")
    row = scinfo.schoolInfo[1].row[0]

    AE = row.ATPT_OFCDC_SC_CODE  # 교육청 코드
    SE = row.SD_SCHUL_CODE  # 학교 코드

    # 학교 코드와 교육청 코드로 2022년 5월 23일의 급식 정보 요청
    scmeal = neis.mealServiceDietInfo(
        ATPT_OFCDC_SC_CODE=AE, SD_SCHUL_CODE=SE, MLSV_YMD="20220523"
    )
    row = scmeal.mealServiceDietInfo[1].row[0]
    meal = row.DDISH_NM.replace("<br/>", "\n")  # 줄바꿈으로 만든 뒤 출력

    # 학교 코드와 교육청 코드로 2022년 6월 1일날 학사일정 요청
    scschedule = neis.SchoolSchedule(
        ATPT_OFCDC_SC_CODE=AE, SD_SCHUL_CODE=SE, AA_YMD=20220601
    )
    row = scschedule.SchoolSchedule[1].row[0]
    schedule = row.EVENT_NM  # 학사일정명 가져옴

    # 학교 코드와 교육청 코드로 초등학교의 2022년 5월 23일의 시간표가져옴
    sctimetable = neis.elsTimetable(
        ATPT_OFCDC_SC_CODE=AE,
        SD_SCHUL_CODE=SE,
        AY="2022",
        SEM="1",
        ALL_TI_YMD=20220523,
        GRADE="1",
        PERIO=1,
    )
    timetable = [i.ITRT_CNTNT for i in sctimetable.elsTimetable[1].row]  # 리스트로 만듦

    academyinfo = neis.acaInsTiInfo(ATPT_OFCDC_SC_CODE=AE)  # 교육청 코드로 학원및 교습소 정보 요청
    academy = academyinfo.acaInsTiInfo[1].row[0].ACA_NM  # 학교이름 출력

    scclass = neis.classInfo(
        ATPT_OFCDC_SC_CODE=AE, SD_SCHUL_CODE=SE, GRADE="1"
    )  # 학교 코드와 교육청 코드로 1학년의 모든 반 정보 요청
    class_info = [i.CLASS_NM for i in scclass.classInfo[1].row]  # 리스트로 만듦

    hiscinfo = neis.schoolInfo(SCHUL_NM="인천기계")  # 다른 정보를 위해 공고로 가져옴
    hirow = hiscinfo.schoolInfo[1].row[0]
    hAE = hirow.ATPT_OFCDC_SC_CODE  # 교육청 코드
    hSE = hirow.SD_SCHUL_CODE  # 학교 코드

    scmajorinfo = neis.schoolMajorinfo(
        ATPT_OFCDC_SC_CODE=hAE, SD_SCHUL_CODE=hSE
    )  # 학과 정보 요청
    majorinfo = [m.DDDEP_NM for m in scmajorinfo.schoolMajorinfo[1].row]  # 리스트로 만듦

    scAflcoinfo = neis.schulAflcoinfo(
        ATPT_OFCDC_SC_CODE=hAE, SD_SCHUL_CODE=hSE
    )  # 학교 계열 정보 요청
    Aflco = [a.ORD_SC_NM for a in scAflcoinfo.schulAflcoinfo[1].row]

    sctiClrm = neis.tiClrminfo(
        ATPT_OFCDC_SC_CODE=hAE, SD_SCHUL_CODE=hSE
    )  # 시간표 강의실 정보 요청
    tiClem = [t.CLRM_NM for t in sctiClrm.tiClrminfo[1].row]

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

## 요청 인자 및 반환 값

[데이터셋](https://open.neis.go.kr/portal/data/dataset/searchDatasetPage.do)을 참고해주세요.

반환되는 객체의 경우 docstring이 적용되어있어 vscode와 같은 텍스트 에디터나 IDE에서 속성을 확인할 수 있습니다.

위의 예제를 참고해주세요.
