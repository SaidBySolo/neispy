import datetime
from .http import Http
from .model import *
from .error import ArgumentError

n = datetime.datetime.now()
now = f'{n.year}{n.month}{n.day}'


class AsyncClient:
    def __init__(self, KEY='', Type='json', pIndex: str = 1, pSize: str = 100):
        """필수인자값을 받습니다

        Keyword Arguments:

            ``KEY`` {str} -- API키를 받습니다. 없을시 샘플키로 요청합니다. (default: {''})

            ``Type`` {str} -- json 또는 xml로 요청이 가능하지만 xml로 바꿀시 작동이 안됩니다. (default: {'json'})

            ``pIndex`` {str} -- 페이지 위치입니다. 샘플키는 1 고정입니다. (default: {1})

            ``pSize`` {str} -- 페이지당 신청숫자 입니다. 샘플키는 5 고정입니다. (default: {100})
        """
        self.http = Http(KEY, Type, pIndex, pSize)

    async def schoolInfo(self, ATPT_OFCDC_SC_CODE: str = None,  SD_SCHUL_CODE: str = None, SCHUL_NM: str = None,
                         SCHUL_KND_SC_NM: str = None, LCTN_SC_NM: str = None, FOND_SC_NM: str = None, rawdata: bool = False):
        """학교기본정보를 요청합니다.

        학교 기본정보에 대한 학교명, 소재지, 주소, 전화번호, 홈페이지주소, 남녀공학여부, 주야구분, 개교기념일, 폐교여부 등을 확인할 수 있는 현황입니다.

        Keyword Arguments:

            `ATPT_OFCDC_SC_CODE` {str} -- 시도교육청코드 (default: {None})

            `SD_SCHUL_CODE` {str} -- 표준학교코드 (default: {None})

            `SCHUL_NM` {str} -- 학교명 (default: {None})

            `SCHUL_KND_SC_NM` {str} -- 학교종류명 (default: {None})

            `LCTN_SC_NM` {str} -- 소재지명 (default: {None})

            `FOND_SC_NM` {str} -- 설립명 (default: {None})

            `rawdata` {bool} -- 여러개의 검색결과를 받아올것인지에 대한 여부입니다. (default: {False})

        Returns:

            str -- 요청한값을 json형식으로 반환합니다.
        """

        paramlist = []

        if ATPT_OFCDC_SC_CODE is not None:
            AOSC = f'ATPT_OFCDC_SC_CODE={ATPT_OFCDC_SC_CODE}'
            paramlist.append(AOSC)

        if SD_SCHUL_CODE is not None:
            SSC = f'&SD_SCHUL_CODE={SD_SCHUL_CODE}'
            paramlist.append(SSC)

        if SCHUL_NM is not None:
            SN = f'&SCHUL_NM={SCHUL_NM}'
            paramlist.append(SN)

        if SCHUL_KND_SC_NM is not None:
            SKSN = f'&SCHUL_KND_SC_NM={SCHUL_KND_SC_NM}'
            paramlist.append(SKSN)

        if LCTN_SC_NM is not None:
            LSN = f'&LCTN_SC_NM={LCTN_SC_NM}'
            paramlist.append(LSN)

        if FOND_SC_NM is not None:
            FSN = f'&FOND_SC_NM={FOND_SC_NM}'
            paramlist.append(FSN)

        query = "".join(paramlist)  # IDK

        data = await self.http.schoolInfo(query)
        return SchoolInfo(data, 'schoolInfo', rawdata)

    async def mealServiceDietInfo(self, ATPT_OFCDC_SC_CODE: str = None, SD_SCHUL_CODE: str = None,
                                  MMEAL_SC_CODE: str = None, MLSV_YMD: int = now, MLSV_FROM_YMD: int = None, MLSV_TO_YMD: int = None, rawdata: bool = False):
        """급식 식단정보를 요청합니다.

        Keyword Arguments:

            `ATPT_OFCDC_SC_CODE` {str} -- 시도교육청코드 (default: {None})

            `SD_SCHUL_CODE` {str} -- 표준학교코드 (default: {None})

            `MMEAL_SC_CODE` {str} -- 식사코드 (default: {None})

            `MLSV_YMD` {int} -- 급식일자(주어지지 않았을경우 사용자의 현재날짜로 요청합니다.) (default: {now})

            `MLSV_FROM_YMD` {int} -- 급식시작일자 (default: {None})

            `MLSV_TO_YMD` {int} -- 급식종료일자 (default: {None})

        Returns:

            str -- 요청한값을 json형식으로 반환합니다.
        """

        paramlist = []

        if ATPT_OFCDC_SC_CODE is not None:
            AOSC = f'&ATPT_OFCDC_SC_CODE={ATPT_OFCDC_SC_CODE}'
            paramlist.append(AOSC)

        if SD_SCHUL_CODE is not None:
            ASC = f'&SD_SCHUL_CODE={SD_SCHUL_CODE}'
            paramlist.append(ASC)

        if MLSV_YMD is not None:
            MY = f'&MLSV_YMD={MLSV_YMD}'
            paramlist.append(MY)

        if MLSV_FROM_YMD is not None:
            MFY = f'&MLSV_FROM_YMD={MLSV_FROM_YMD}'
            paramlist.append(MFY)

        if MLSV_TO_YMD is not None:
            MTY = f'&MLSV_TO_YMD={MLSV_TO_YMD}'
            paramlist.append(MTY)

        query = "".join(paramlist)

        data = await self.http.mealServiceDietInfo(query)
        return MealServiceDietInfo(data, 'mealServiceDietInfo', rawdata)

    async def SchoolSchedule(self, ATPT_OFCDC_SC_CODE: str = None, SD_SCHUL_CODE: str = None, DGHT_CRSE_SC_NM: str = None,
                             SCHUL_CRSE_SC_NM: str = None, AA_YMD: int = now, AA_FROM_YMD: int = None, AA_TO_YMD: int = None, rawdata: bool = False):
        """학사일정입니다.

        학년도, 학교별 주요 행사 정보에 대한 학사일자, 행사명, 행사내용, 학년별 행사여부 등의 현황입니다.

        Keyword Arguments:

            `ATPT_OFCDC_SC_CODE` {str} -- 시도교육청코드 (default: {None})

            `SD_SCHUL_CODE` {str} -- 표준학교코드 (default: {None})

            `DGHT_CRSE_SC_NM` {str} -- 주야과정명 (default: {None})

            `SCHUL_CRSE_SC_NM` {str} -- 학교과정명 (default: {None})

            `AA_YMD` {int} -- 학사일자(주어지지 않았을경우 사용자의 현재날짜로 요청합니다.) (default: {now})

            `AA_FROM_YMD` {int} -- 학사시작일자 (default: {None})

            `AA_TO_YMD` {int} -- 학사종료일자 (default: {None})

        Returns:

            str -- 요청한값을 json형식으로 반환합니다.
        """

        paramlist = []

        if ATPT_OFCDC_SC_CODE is not None:
            AOSC = f'&ATPT_OFCDC_SC_CODE={ATPT_OFCDC_SC_CODE}'
            paramlist.append(AOSC)

        if SD_SCHUL_CODE is not None:
            ASC = f'&SD_SCHUL_CODE={SD_SCHUL_CODE}'
            paramlist.append(ASC)

        if DGHT_CRSE_SC_NM is not None:
            DCSN = f'&DGHT_CRSE_SC_NM={DGHT_CRSE_SC_NM}'
            paramlist.append(DCSN)

        if SCHUL_CRSE_SC_NM is not None:
            SCSN = f'&SCHUL_CRSE_SC_NM={SCHUL_CRSE_SC_NM}'
            paramlist.append(SCSN)

        if AA_YMD is not None:
            AY = f'&AA_YMD={AA_YMD}'
            paramlist.append(AY)

        if AA_FROM_YMD is not None:
            AFY = f'&AA_FROM_YMD={AA_FROM_YMD}'
            paramlist.append(AFY)

        if AA_TO_YMD is not None:
            ATY = f'&AA_TO_YMD={AA_TO_YMD}'
            paramlist.append(ATY)

        query = "".join(paramlist)

        data = await self.http.SchoolSchedule(query)
        return SchoolSchedule(data, 'SchoolSchedule', rawdata)

    async def acaInsTiInfo(self, ATPT_OFCDC_SC_CODE: str = None, ADMST_ZONE_NM: str = None,
                           ACA_ASNUM: str = None, REALM_SC_NM: str = None, LE_ORD_NM: str = None, LE_CRSE_NM: str = None, rawdata: bool = False):
        """학원교습소정보 입니다.

        개설되어있는 학원 및 교습소의 학원명, 휴원일자, 등록상태, 정원, 분야, 계열 및 과정등을 확인할 수 있으며

        수강료 공개여부에 따라 수강료 내용을 확인할 수 있습니다.


        Keyword Arguments:

            `ATPT_OFCDC_SC_CODE` {str} -- 시도교육청코드 (default: {None})

            `ADMST_ZONE_NM` {str} -- 행정구역명 (default: {None})

            `ACA_ASNUM` {str} -- 학원지정번호 (default: {None})

            `REALM_SC_NM` {str} -- 분야명 (default: {None})

            `LE_ORD_NM` {str} -- 교습계열명 (default: {None})

            `LE_CRSE_NM` {str} -- 교습과정명 (default: {None})

        Returns:

            str -- 요청한값을 json형식을 반환합니다.
        """

        paramlist = []

        if ATPT_OFCDC_SC_CODE is not None:
            AOSC = f'&ATPT_OFCDC_SC_CODE={ATPT_OFCDC_SC_CODE}'
            paramlist.append(AOSC)

        if ADMST_ZONE_NM is not None:
            AZN = f'&ADMST_ZONE_NM={ADMST_ZONE_NM}'
            paramlist.append(AZN)

        if ACA_ASNUM is not None:
            AA = f'ACA_ASNUM={ACA_ASNUM}'
            paramlist.append(AA)

        if REALM_SC_NM is not None:
            RSC = f'REALM_SC_NM={REALM_SC_NM}'
            paramlist.append(RSC)

        if LE_ORD_NM is not None:
            LON = f'LE_ORD_NM={LE_ORD_NM}'
            paramlist.append(LON)

        if LE_CRSE_NM is not None:
            LCN = f'LE_CRSE_NM={LE_CRSE_NM}'
            paramlist.append(LCN)

        query = "".join(paramlist)

        data = await self.http.acaInsTiInfo(query)
        return AcaInsTiInfo(data, 'acaInsTiInfo', rawdata)

    async def timeTable(self, schclass: str, ATPT_OFCDC_SC_CODE: str = None,
                        SD_SCHUL_CODE: str = None, AY: int = None, SEM: int = None, ALL_TI_YMD: int = now,
                        GRADE: int = None, CLASS_NM: str = None, PERIO: int = None, TI_FROM_YMD: int = None, TI_TO_YMD: int = None, rawdata: bool = True):
        """초,중,고 시간표

        초등학교,중학교,고등학교 학년도, 학교, 학기, 학년, 반, 교시별 시간표 수업내용을 확인할 수 있는 현황입니다

        Arguments:

            schclass {str} -- 초등학교(els),중학교(mis),고등학교(his)중 선택을 하는 인자입니다.

        Keyword Arguments:

            `ATPT_OFCDC_SC_CODE` {str} -- 시도교육청코드 (default: {None})

            `SD_SCHUL_CODE` {str} -- 표준학교코드 (default: {None})

            `AY` {int} -- 학년도 (default: {None})

            `SEM` {int} -- 학기 (default: {None})

            `ALL_TI_YMD` {int} -- 시간표일자(주어지지 않았을경우 사용자의 현재날짜로 요청합니다.) (default: {now})

            `GRADE` {int} --학년 (default: {None})

            `CLASS_NM` {str} -- 반명 (default: {None})

            `PERIO` {int} -- 교시 (default: {None})

            `TI_FROM_YMD` {int} -- 시간표시작일자 (default: {None})

            `TI_TO_YMD` {int} -- 시간표종료일자 (default: {None})

        Raises:

            ArgumentError: ``schclass``의 받은 인자중 일치한것이 없으면 raise합니다.

        Returns:

            str -- 요청한값을 json형식을 반환합니다.
        """
        arg = ['els', 'mis', 'his', 'sps']
        paramlist = []

        if ATPT_OFCDC_SC_CODE is not None:
            AOSC = f'&ATPT_OFCDC_SC_CODE={ATPT_OFCDC_SC_CODE}'
            paramlist.append(AOSC)

        if SD_SCHUL_CODE is not None:
            ASC = f'&SD_SCHUL_CODE={SD_SCHUL_CODE}'
            paramlist.append(ASC)

        if AY is not None:
            AY = f'&AY={AY}'
            paramlist.append(AY)

        if SEM is not None:
            SEM = f'&SEM={SEM}'
            paramlist.append(SEM)

        if ALL_TI_YMD is not None:
            ATY = f'&ALL_TI_YMD={ALL_TI_YMD}'
            paramlist.append(ATY)

        if GRADE is not None:
            GE = f'&GRADE={GRADE}'
            paramlist.append(GE)

        if CLASS_NM is not None:
            CN = f'&CLASS_NM={CLASS_NM}'
            paramlist.append(CN)

        if PERIO is not None:
            PO = f'&PERIO={PERIO}'
            paramlist.append(PO)

        if TI_FROM_YMD is not None:
            TFY = f'&TI_FROM_YMD={TI_FROM_YMD}'
            paramlist.append(TFY)

        if TI_TO_YMD is not None:
            TTY = f'&TI_TO_YMD={TI_TO_YMD}'
            paramlist.append(TTY)

        query = "".join(paramlist)

        if schclass in arg:
            data = await self.http.timeTable(schclass, query)
            return TimeTable(data, schclass + "Timetable", rawdata)
        else:
            raise ArgumentError

    async def classInfo(self, ATPT_OFCDC_SC_CODE: str = None, SD_SCHUL_CODE: str = None, AY: str = None,
                        GRADE: str = None, DGHT_CRSE_SC_NM: str = None, SCHUL_CRSE_SC_NM: str = None, ORD_SC_NM: str = None, DDDEP_NM: str = None, rawdata: bool = True):

        paramlist = []

        if ATPT_OFCDC_SC_CODE is not None:
            AOSC = f'&ATPT_OFCDC_SC_CODE={ATPT_OFCDC_SC_CODE}'
            paramlist.append(AOSC)

        if SD_SCHUL_CODE is not None:
            SSC = f'&SD_SCHUL_CODE={SD_SCHUL_CODE}'
            paramlist.append(SSC)

        if AY is not None:
            AY = f'&AY={AY}'
            paramlist.append(AY)

        if GRADE is not None:
            GE = f'&GE={GRADE}'
            paramlist.append(GE)

        if DGHT_CRSE_SC_NM is not None:
            DCSN = f'&DGHT_CRSE_SCNM={DGHT_CRSE_SC_NM}'
            paramlist.append(DCSN)

        if SCHUL_CRSE_SC_NM is not None:
            SCSN = f'&SCHUL_CRSE_SC_NM={SCHUL_CRSE_SC_NM}'
            paramlist.append(SCSN)

        if ORD_SC_NM is not None:
            OSN = f'&ORD_SC_NM={ORD_SC_NM}'
            paramlist.append(OSN)

        if DDDEP_NM is not None:
            DN = f'&DDDEP_NM={DDDEP_NM}'
            paramlist.append(DN)

        query = "".join(paramlist)

        data = await self.http.classInfo(query)
        return ClassInfo(data, 'classInfo', rawdata)

    async def schoolMajorinfo(self, ATPT_OFCDC_SC_CODE: str = None, SD_SCHUL_CODE: str = None,
                              DGHT_CRSE_SC_NM: str = None, ORD_SC_NM: str = None, rawdata: bool = True):

        paramlist = []

        if ATPT_OFCDC_SC_CODE is not None:
            AOSC = f'&ATPT_OFCDC_SC_CODE={ATPT_OFCDC_SC_CODE}'
            paramlist.append(AOSC)

        if SD_SCHUL_CODE is not None:
            SSC = f'&SD_SCHUL_CODE={SD_SCHUL_CODE}'
            paramlist.append(SSC)

        if DGHT_CRSE_SC_NM is not None:
            DCSN = f'&DGHT_CRSE_SC_NM={DGHT_CRSE_SC_NM}'
            paramlist.append(DCSN)

        if ORD_SC_NM is not None:
            OSN = f'&ORD_SC_NM={ORD_SC_NM}'
            paramlist.append(OSN)

        query = "".join(paramlist)

        data = await self.http.schoolMajorinfo(query)
        return SchoolMajorInfo(data, 'schoolMajorinfo', rawdata)

    async def schulAflcoinfo(self, ATPT_OFCDC_SC_CODE: str = None, SD_SCHUL_CODE: str = None,
                             DGHT_CRSE_SC_NM: str = None, rawdata: bool = True):

        paramlist = []

        if ATPT_OFCDC_SC_CODE is not None:
            AOSC = f'&ATPT_OFCDC_SC_CODE={ATPT_OFCDC_SC_CODE}'
            paramlist.append(AOSC)

        if SD_SCHUL_CODE is not None:
            SSC = f'&SD_SCHUL_CODE={SD_SCHUL_CODE}'
            paramlist.append(SSC)

        if DGHT_CRSE_SC_NM is not None:
            DCSN = f'&DGHT_CRSE_SC_NM={DGHT_CRSE_SC_NM}'
            paramlist.append(DCSN)

        query = "".join(paramlist)

        data = await self.http.schulAflcoinfo(query)
        return SchulAflcoInfo(data, 'schulAflcoinfo', rawdata)

    async def tiClrminfo(self, ATPT_OFCDC_SC_CODE: str = None, SD_SCHUL_CODE: str = None, AY: str = None,
                         GRADE: str = None, SEM: str = None, SCHUL_CRSE_SC_NM: str = None, DGHT_CRSE_SC_NM: str = None,
                         ORD_SC_NM: str = None, DDDEP_NM: str = None, rawdata: bool = True):

        paramlist = []

        if ATPT_OFCDC_SC_CODE is not None:
            AOSC = f'&ATPT_OFCDC_SC_CODE={ATPT_OFCDC_SC_CODE}'
            paramlist.append(AOSC)

        if SD_SCHUL_CODE is not None:
            SSC = f'&SD_SCHUL_CODE={SD_SCHUL_CODE}'
            paramlist.append(SSC)

        if AY is not None:
            AY = f'&AY={AY}'
            paramlist.append(AY)

        if GRADE is not None:
            GE = f'&GE={GRADE}'
            paramlist.append(GE)

        if SEM is not None:
            SM = f'&SEM={SEM}'
            paramlist.append(SM)

        if DGHT_CRSE_SC_NM is not None:
            DCSN = f'&DGHT_CRSE_SCNM={DGHT_CRSE_SC_NM}'
            paramlist.append(DCSN)

        if SCHUL_CRSE_SC_NM is not None:
            SCSN = f'&SCHUL_CRSE_SC_NM={SCHUL_CRSE_SC_NM}'
            paramlist.append(SCSN)

        if ORD_SC_NM is not None:
            OSN = f'&ORD_SC_NM={ORD_SC_NM}'
            paramlist.append(OSN)

        if DDDEP_NM is not None:
            DN = f'&DDDEP_NM={DDDEP_NM}'
            paramlist.append(DN)

        query = "".join(paramlist)

        data = await self.http.tiClrminfo(query)
        return TiClrmInfo(data, 'tiClrminfo', rawdata)
