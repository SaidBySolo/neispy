from neispy.sync import SyncNeispy


def test_all(client: SyncNeispy):
    scinfo = client.schoolInfo(SCHUL_NM="인천석천초등학교")
    AE = scinfo[0].ATPT_OFCDC_SC_CODE  # 교육청코드
    SE = scinfo[0].SD_SCHUL_CODE  # 학교코드

    # 학교코드와 교육청 코드로 2019년 1월 22일의 급식 정보 요청
    scmeal = client.mealServiceDietInfo(AE, SE, MLSV_YMD="20190122")
    meal = scmeal[0].DDISH_NM.replace("<br/>", "\n")  # 줄바꿈으로 만든뒤 출력

    # 학교코드와 교육청 코드로 2019년 3월 7일날 학사일정 요청
    scschedule = client.SchoolSchedule(AE, SE, AA_YMD=20201002)
    schedule = scschedule[0].EVENT_NM  # 학사일정명 가져옴

    # 학교코드와 교육청 코드로 초등학교의 2020년 1월 22일의 시간표가져옴
    sctimetable = client.elsTimetable(AE, SE, 2019, 2, 20200122, "1", "1")
    timetable = [i.ITRT_CNTNT for i in sctimetable]  # 리스트로 만듬

    academyinfo = client.acaInsTiInfo(AE)  # 교육청 코드로 학원및 교습소 정보 요청
    academy = academyinfo[0].ACA_NM  # 학교이름 출력

    scclass = client.classInfo(AE, SE, GRADE="1")  # 학교코드와 교육청 코드로 1학년의 모든 반정보 요청
    class_info = [i.CLASS_NM for i in scclass]  # 리스트로만듬

    hiscinfo = client.schoolInfo(SCHUL_NM="인천기계")  # 다른정보를 위해 공고로 가져옴
    hAE = hiscinfo[0].ATPT_OFCDC_SC_CODE  # 교육청코드
    hSE = hiscinfo[0].SD_SCHUL_CODE  # 학교코드

    scmajorinfo = client.schoolMajorinfo(hAE, hSE)  # 학과정보 요청
    majorinfo = [m.DDDEP_NM for m in scmajorinfo]  # 리스트로 만듬

    scAflcoinfo = client.schulAflcoinfo(hAE, hSE)  # 학교 계열정보 요청
    Aflco = [a.ORD_SC_NM for a in scAflcoinfo]

    sctiClrm = client.tiClrminfo(hAE, hSE)  # 시간표 강의실 정보 요청
    tiClem = [t.CLRM_NM for t in sctiClrm]

    assert meal
    assert schedule
    assert timetable
    assert academy
    assert class_info
    assert majorinfo
    assert Aflco
    assert tiClem
