import asyncio
import datetime
import functools
from typing import Any

import aiohttp

from .error import (
    ArgumentError,
    AuthenticationKeyInvaild,
    CannotExceed1000,
    DailyTrafficLimit,
    DatabaseConnectionError,
    DataNotFound,
    HTTPException,
    LimitUseAuthenticationkey,
    LocationValueTypeInvaild,
    MissingRequiredValues,
    ServerError,
    ServiceNotFound,
    SQLStatementError,
)
from .model import (
    AcaInsTiInfo,
    ClassInfo,
    MealServiceDietInfo,
    SchoolInfo,
    SchoolMajorInfo,
    SchoolSchedule,
    SchulAflcoInfo,
    TiClrmInfo,
    TimeTable,
)
from .utils import concatDict

HTTPExceptions = {
    "INFO-200": DataNotFound,
    "INFO-300": LimitUseAuthenticationkey,
    "ERROR-290": AuthenticationKeyInvaild,
    "ERROR-300": MissingRequiredValues,
    "ERROR-310": ServiceNotFound,
    "ERROR-333": LocationValueTypeInvaild,
    "ERROR-336": CannotExceed1000,
    "ERROR-337": DailyTrafficLimit,
    "ERROR-500": ServerError,
    "ERROR-600": DatabaseConnectionError,
    "ERROR-601": SQLStatementError,
}


KST = datetime.timezone(datetime.timedelta(hours=9))


def now():
    return datetime.datetime.now(tz=KST).strftime("%Y%m%d")


class _Client:
    BASE = "https://open.neis.go.kr/hub"

    def __init__(self, KEY: str = None, pIndex: int = 1, pSize: int = 100) -> None:
        """필수인자값을 받습니다

        Keyword Arguments:

            ``KEY`` {str} -- API키를 받습니다. 없을시 샘플키로 요청합니다. (default: {''})

            ``pIndex`` {int} -- 페이지 위치입니다. 샘플키는 1 고정입니다. (default: {1})

            ``pSize`` {int} -- 페이지당 신청숫자 입니다. 샘플키는 5 고정입니다. (default: {100})
        """

        self.KEY = KEY
        if not KEY:
            import warnings

            warnings.warn("API키가 없습니다, 샘플키로 요청합니다", UserWarning)

        self.pIndex = pIndex
        self.pSize = pSize

    async def request(self, method: str, endpoint: str, **kwargs):
        URL = self.BASE + endpoint

        if not "params" in kwargs:
            kwargs["params"] = {}

        if self.KEY:
            kwargs["params"]["KEY"] = self.KEY
        kwargs["params"]["Type"] = "json"
        kwargs["params"]["pindex"] = self.pIndex
        kwargs["params"]["pSize"] = self.pSize

        async with aiohttp.ClientSession() as session:
            async with session.request(method, URL, **kwargs) as response:
                Data = await response.json(content_type=None)

                if isinstance(Data.get("RESULT", []), list):
                    Data = concatDict(list(Data.values())[0])

                HeadData = (
                    concatDict(Data["head"])["RESULT"]
                    if "head" in Data
                    else Data["RESULT"]
                )

                Code, Msg = HeadData["CODE"], HeadData["MESSAGE"]

                if Code == "INFO-000":
                    return Data["row"]

                raise HTTPExceptions.get(Code, HTTPException)(Code, Msg)

    async def schoolInfo(
        self,
        ATPT_OFCDC_SC_CODE: str = None,
        SD_SCHUL_CODE: str = None,
        SCHUL_NM: str = None,
        SCHUL_KND_SC_NM: str = None,
        LCTN_SC_NM: str = None,
        FOND_SC_NM: str = None,
    ) -> SchoolInfo:
        """학교기본정보를 요청합니다.

        학교 기본정보에 대한 학교명, 소재지, 주소, 전화번호, 홈페이지주소, 남녀공학여부, 주야구분, 개교기념일, 폐교여부 등을 확인할 수 있는 현황입니다.

        Keyword Arguments:

            `ATPT_OFCDC_SC_CODE` {str} -- 시도교육청코드 (default: {None})

            `SD_SCHUL_CODE` {str} -- 표준학교코드 (default: {None})

            `SCHUL_NM` {str} -- 학교명 (default: {None})

            `SCHUL_KND_SC_NM` {str} -- 학교종류명 (default: {None})

            `LCTN_SC_NM` {str} -- 소재지명 (default: {None})

            `FOND_SC_NM` {str} -- 설립명 (default: {None})

        Returns:

            SchoolInfo -- 요청한값을반환합니다.
        """

        params = {}
        if ATPT_OFCDC_SC_CODE:
            params["ATPT_OFCDC_SC_CODE"] = ATPT_OFCDC_SC_CODE
        if SD_SCHUL_CODE:
            params["SD_SCHUL_CODE"] = SD_SCHUL_CODE
        if SCHUL_NM:
            params["SCHUL_NM"] = SCHUL_NM
        if SCHUL_KND_SC_NM:
            params["SCHUL_KND_SC_NM"] = SCHUL_KND_SC_NM
        if LCTN_SC_NM:
            params["LCTN_SC_NM"] = LCTN_SC_NM
        if FOND_SC_NM:
            params["FOND_SC_NM"] = FOND_SC_NM

        Data = await self.request("GET", "/schoolInfo", params=params)
        return SchoolInfo(Data)

    async def mealServiceDietInfo(
        self,
        ATPT_OFCDC_SC_CODE: str = None,
        SD_SCHUL_CODE: str = None,
        MMEAL_SC_CODE: str = None,
        MLSV_YMD: str = now(),
        MLSV_FROM_YMD: str = None,
        MLSV_TO_YMD: str = None,
    ) -> MealServiceDietInfo:
        """급식 식단정보를 요청합니다.

        Keyword Arguments:

            `ATPT_OFCDC_SC_CODE` {str} -- 시도교육청코드 (default: {None})

            `SD_SCHUL_CODE` {str} -- 표준학교코드 (default: {None})

            `MMEAL_SC_CODE` {str} -- 식사코드 (default: {None})

            `MLSV_YMD` {str} -- 급식일자(주어지지 않았을경우 사용자의 현재날짜로 요청합니다.) (default: {now})

            `MLSV_FROM_YMD` {str} -- 급식시작일자 (default: {None})

            `MLSV_TO_YMD` {str} -- 급식종료일자 (default: {None})

        Returns:

            MealServiceDietInfo -- 요청한값을 반환합니다.
        """

        params = {}
        if ATPT_OFCDC_SC_CODE:
            params["ATPT_OFCDC_SC_CODE"] = ATPT_OFCDC_SC_CODE
        if SD_SCHUL_CODE:
            params["SD_SCHUL_CODE"] = SD_SCHUL_CODE
        if MMEAL_SC_CODE:
            params["MMEAL_SC_CODE"] = MMEAL_SC_CODE
        if MLSV_YMD:
            params["MLSV_YMD"] = MLSV_YMD
        if MLSV_FROM_YMD:
            params["MLSV_FROM_YMD"] = MLSV_FROM_YMD
        if MLSV_TO_YMD:
            params["MLSV_TO_YMD"] = MLSV_TO_YMD

        Data = await self.request("GET", "/mealServiceDietInfo", params=params)
        return MealServiceDietInfo(Data)

    async def SchoolSchedule(
        self,
        ATPT_OFCDC_SC_CODE: str = None,
        SD_SCHUL_CODE: str = None,
        DGHT_CRSE_SC_NM: str = None,
        SCHUL_CRSE_SC_NM: str = None,
        AA_YMD: int = now(),
        AA_FROM_YMD: int = None,
        AA_TO_YMD: int = None,
    ) -> SchoolSchedule:
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

            SchoolSchedule -- 요청한값을 반환합니다.
        """

        params = {}
        if ATPT_OFCDC_SC_CODE:
            params["ATPT_OFCDC_SC_CODE"] = ATPT_OFCDC_SC_CODE
        if SD_SCHUL_CODE:
            params["SD_SCHUL_CODE"] = SD_SCHUL_CODE
        if DGHT_CRSE_SC_NM:
            params["DGHT_CRSE_SC_NM"] = DGHT_CRSE_SC_NM
        if SCHUL_CRSE_SC_NM:
            params["SCHUL_CRSE_SC_NM"] = SCHUL_CRSE_SC_NM
        if AA_YMD:
            params["AA_YMD"] = AA_YMD
        if AA_FROM_YMD:
            params["AA_FROM_YMD"] = AA_FROM_YMD
        if AA_TO_YMD:
            params["AA_TO_YMD"] = AA_TO_YMD

        Data = await self.request("GET", "/SchoolSchedule", params=params)
        return SchoolSchedule(Data)

    async def acaInsTiInfo(
        self,
        ATPT_OFCDC_SC_CODE: str = None,
        ADMST_ZONE_NM: str = None,
        ACA_ASNUM: str = None,
        REALM_SC_NM: str = None,
        LE_ORD_NM: str = None,
        LE_CRSE_NM: str = None,
    ) -> AcaInsTiInfo:
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

            AcaInsTiInfo -- 요청한값을 반환합니다.
        """

        params = {}
        if ATPT_OFCDC_SC_CODE:
            params["ATPT_OFCDC_SC_CODE"] = ATPT_OFCDC_SC_CODE
        if ADMST_ZONE_NM:
            params["ADMST_ZONE_NM"] = ADMST_ZONE_NM
        if ACA_ASNUM:
            params["ACA_ASNUM"] = ACA_ASNUM
        if REALM_SC_NM:
            params["REALM_SC_NM"] = REALM_SC_NM
        if LE_ORD_NM:
            params["LE_ORD_NM"] = LE_ORD_NM
        if LE_CRSE_NM:
            params["LE_CRSE_NM"] = LE_CRSE_NM

        Data = await self.request("GET", "/acaInsTiInfo", params=params)
        return AcaInsTiInfo(Data)

    async def timeTable(
        self,
        schclass: str,
        ATPT_OFCDC_SC_CODE: str = None,
        SD_SCHUL_CODE: str = None,
        AY: int = None,
        SEM: int = None,
        ALL_TI_YMD: int = now(),
        DGHT_CRSE_SC_NM=None,
        ORD_SC_NM=None,
        DDDEP_NM=None,
        GRADE: int = None,
        CLRM_NM: str = None,
        CLASS_NM: str = None,
        PERIO: int = None,
        TI_FROM_YMD: int = None,
        TI_TO_YMD: int = None,
        SCHUL_CRSE_SC_NM: str = None,
    ) -> TimeTable:
        """초,중,고 시간표

        초등학교,중학교,고등학교 학년도, 학교, 학기, 학년, 반, 교시별 시간표 수업내용을 확인할 수 있는 현황입니다

        Arguments:

            schclass {str} -- 초등학교(els),중학교(mis),고등학교(his),특수학교(sps)중 선택을 하는 인자입니다.

        Keyword Arguments:

            `ATPT_OFCDC_SC_CODE` {str} -- 시도교육청코드 (default: {None})

            `SD_SCHUL_CODE` {str} -- 표준학교코드 (default: {None})

            `AY` {int} -- 학년도 (default: {None})

            `SEM` {int} -- 학기 (default: {None})

            `ALL_TI_YMD` {int} -- 시간표일자(주어지지 않았을경우 사용자의 현재날짜로 요청합니다.) (default: {now})

            `DGHT_CRSE_SC_NM` {str} -- 주야과정명(고등학교일 경우만 받음) (default: {None})

           ` ORD_SC_NM` {str} -- 계열명(고등학교일 경우만 받음) (default: {None})

            `DDDEP_NM` {str} -- 학과명(고등학교일 경우만 받음) (default: {None})

            `GRADE` {int} -- 학년 (default: {None})

            `CLRM_NM` {str} -- 강의실명(고등학교일 경우만 받음) (default: {None})

            `CLASS_NM` {str} -- 반명 (default: {None})

            `PERIO` {int} -- 교시 (default: {None})

            `TI_FROM_YMD` {int} -- 시간표시작일자 (default: {None})

            `TI_TO_YMD` {int} -- 시간표종료일자 (default: {None})

            `SCHUL_CRSE_SC_NM` {str} -- 과정명(특수학교일 경우만 받음) (default: {None})

        Raises:

            ArgumentError: ``schclass``의 받은 인자중 일치한것이 없으면 raise합니다.

        Returns:

            TimeTable -- 요청한값을 반환합니다.
        """

        if not schclass in ["els", "mis", "his", "sps"]:
            raise ArgumentError

        params = {}
        if ATPT_OFCDC_SC_CODE:
            params["ATPT_OFCDC_SC_CODE"] = ATPT_OFCDC_SC_CODE
        if SD_SCHUL_CODE:
            params["SD_SCHUL_CODE"] = SD_SCHUL_CODE
        if AY:
            params["AY"] = AY
        if SEM:
            params["SEM"] = SEM
        if ALL_TI_YMD:
            params["ALL_TI_YMD"] = ALL_TI_YMD
        if DGHT_CRSE_SC_NM:
            params["DGHT_CRSE_SCNM"] = DGHT_CRSE_SC_NM
        if ORD_SC_NM:
            params["ORD_SC_NM"] = ORD_SC_NM
        if DDDEP_NM:
            params["DDDEP_NM"] = DDDEP_NM
        if GRADE:
            params["GRADE"] = GRADE
        if CLRM_NM:
            params["CLRM_NM"] = CLRM_NM
        if CLASS_NM:
            params["CLASS_NM"] = CLASS_NM
        if PERIO:
            params["PERIO"] = PERIO
        if TI_FROM_YMD:
            params["TI_FROM_YMD"] = TI_FROM_YMD
        if TI_TO_YMD:
            params["TI_TO_YMD"] = TI_TO_YMD
        if SCHUL_CRSE_SC_NM:
            params["SCHUL_CRSE_SC_NM"] = SCHUL_CRSE_SC_NM

        Data = await self.request("GET", f"/{schclass}Timetable", params=params)
        return TimeTable(Data)

    async def classInfo(
        self,
        ATPT_OFCDC_SC_CODE: str = None,
        SD_SCHUL_CODE: str = None,
        AY: str = None,
        GRADE: str = None,
        DGHT_CRSE_SC_NM: str = None,
        SCHUL_CRSE_SC_NM: str = None,
        ORD_SC_NM: str = None,
        DDDEP_NM: str = None,
    ) -> ClassInfo:

        params = {}
        if ATPT_OFCDC_SC_CODE:
            params["ATPT_OFCDC_SC_CODE"] = ATPT_OFCDC_SC_CODE
        if SD_SCHUL_CODE:
            params["SD_SCHUL_CODE"] = SD_SCHUL_CODE
        if AY:
            params["AY"] = AY
        if GRADE:
            params["GRADE"] = GRADE
        if DGHT_CRSE_SC_NM:
            params["DGHT_CRSE_SCNM"] = DGHT_CRSE_SC_NM
        if SCHUL_CRSE_SC_NM:
            params["SCHUL_CRSE_SC_NM"] = SCHUL_CRSE_SC_NM
        if ORD_SC_NM:
            params["ORD_SC_NM"] = ORD_SC_NM
        if DDDEP_NM:
            params["DDDEP_NM"] = DDDEP_NM

        Data = await self.request("GET", "/classInfo", params=params)
        return ClassInfo(Data)

    async def schoolMajorinfo(
        self,
        ATPT_OFCDC_SC_CODE: str = None,
        SD_SCHUL_CODE: str = None,
        DGHT_CRSE_SC_NM: str = None,
        ORD_SC_NM: str = None,
    ) -> SchoolMajorInfo:

        params = {}
        if ATPT_OFCDC_SC_CODE:
            params["ATPT_OFCDC_SC_CODE"] = ATPT_OFCDC_SC_CODE
        if SD_SCHUL_CODE:
            params["SD_SCHUL_CODE"] = SD_SCHUL_CODE
        if DGHT_CRSE_SC_NM:
            params["DGHT_CRSE_SCNM"] = DGHT_CRSE_SC_NM
        if ORD_SC_NM:
            params["ORD_SC_NM"] = ORD_SC_NM

        Data = await self.request("GET", "/schoolMajorinfo", params=params)
        return SchoolMajorInfo(Data)

    async def schulAflcoinfo(
        self,
        ATPT_OFCDC_SC_CODE: str = None,
        SD_SCHUL_CODE: str = None,
        DGHT_CRSE_SC_NM: str = None,
    ) -> SchulAflcoInfo:

        params = {}
        if ATPT_OFCDC_SC_CODE:
            params["ATPT_OFCDC_SC_CODE"] = ATPT_OFCDC_SC_CODE
        if SD_SCHUL_CODE:
            params["SD_SCHUL_CODE"] = SD_SCHUL_CODE
        if DGHT_CRSE_SC_NM:
            params["DGHT_CRSE_SCNM"] = DGHT_CRSE_SC_NM

        Data = await self.request("GET", "/schulAflcoinfo", params=params)
        return SchulAflcoInfo(Data)

    async def tiClrminfo(
        self,
        ATPT_OFCDC_SC_CODE: str = None,
        SD_SCHUL_CODE: str = None,
        AY: str = None,
        GRADE: str = None,
        SEM: str = None,
        SCHUL_CRSE_SC_NM: str = None,
        DGHT_CRSE_SC_NM: str = None,
        ORD_SC_NM: str = None,
        DDDEP_NM: str = None,
    ) -> TiClrmInfo:

        params = {}
        if ATPT_OFCDC_SC_CODE:
            params["ATPT_OFCDC_SC_CODE"] = ATPT_OFCDC_SC_CODE
        if SD_SCHUL_CODE:
            params["SD_SCHUL_CODE"] = SD_SCHUL_CODE
        if AY:
            params["AY"] = AY
        if GRADE:
            params["GRADE"] = GRADE
        if SEM:
            params["SEM"] = SEM
        if SCHUL_CRSE_SC_NM:
            params["SCHUL_CRSE_SC_NM"] = SCHUL_CRSE_SC_NM
        if DGHT_CRSE_SC_NM:
            params["DGHT_CRSE_SCNM"] = DGHT_CRSE_SC_NM
        if ORD_SC_NM:
            params["ORD_SC_NM"] = ORD_SC_NM
        if DDDEP_NM:
            params["DDDEP_NM"] = DDDEP_NM

        Data = await self.request("GET", "/tiClrminfo", params=params)
        return TiClrmInfo(Data)


class Client(_Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.loop = asyncio.get_event_loop()

    def __run_coroutine(self, coroutine, *args, **kwargs):
        if self.loop.is_running():
            return coroutine(*args, **kwargs)

        return self.loop.run_until_complete(coroutine(*args, **kwargs))

    def __getattribute__(self, name: str) -> Any:
        attribute = getattr(super(), name, None)

        if not attribute:
            return object.__getattribute__(self, name)

        if asyncio.iscoroutinefunction(attribute):
            return functools.partial(self.__run_coroutine, attribute)

        return attribute
