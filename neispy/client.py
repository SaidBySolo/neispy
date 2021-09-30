try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal
from neispy.http import NeispyRequest
from typing import Any, Optional
from aiohttp.client import ClientSession


# KST = datetime.timezone(datetime.timedelta(hours=9))


# def now() -> Any:
#     return datetime.datetime.now(tz=KST).strftime("%Y%m%d")


class Neispy(NeispyRequest):
    def __init__(
        self,
        KEY: Optional[str] = None,
        Type: Literal["json", "xml"] = "json",
        pIndex: int = 1,
        pSize: int = 100,
        session: Optional[ClientSession] = None,
    ) -> None:
        super().__init__(
            KEY=KEY, Type=Type, pIndex=pIndex, pSize=pSize, session=session
        )

    def __get_params(self, locals: dict[str, Any]) -> Any:
        locals.pop("self")
        return {k: v for k, v in locals.items() if v is not None}

    async def schoolInfo(
        self,
        ATPT_OFCDC_SC_CODE: Optional[str] = None,
        SD_SCHUL_CODE: Optional[str] = None,
        SCHUL_NM: Optional[str] = None,
        SCHUL_KND_SC_NM: Optional[str] = None,
        LCTN_SC_NM: Optional[str] = None,
        FOND_SC_NM: Optional[str] = None,
    ) -> Any:
        params = self.__get_params(locals())
        return await self.get_schoolInfo(params)

    async def mealServiceDietInfo(
        self,
        ATPT_OFCDC_SC_CODE: Optional[str] = None,
        SD_SCHUL_CODE: Optional[str] = None,
        MMEAL_SC_CODE: Optional[str] = None,
        MLSV_YMD: Optional[str] = None,
        MLSV_FROM_YMD: Optional[str] = None,
        MLSV_TO_YMD: Optional[str] = None,
    ) -> Any:
        params = self.__get_params(locals())
        return await self.get_mealServiceDietInfo(params)

    async def SchoolSchedule(
        self,
        ATPT_OFCDC_SC_CODE: Optional[str] = None,
        SD_SCHUL_CODE: Optional[str] = None,
        DGHT_CRSE_SC_NM: Optional[str] = None,
        SCHUL_CRSE_SC_NM: Optional[str] = None,
        AA_YMD: Optional[int] = None,
        AA_FROM_YMD: Optional[int] = None,
        AA_TO_YMD: Optional[int] = None,
    ) -> Any:
        params = self.__get_params(locals())
        return await self.get_SchoolSchedule(params)

    async def acaInsTiInfo(
        self,
        ATPT_OFCDC_SC_CODE: Optional[str] = None,
        ADMST_ZONE_NM: Optional[str] = None,
        ACA_ASNUM: Optional[str] = None,
        REALM_SC_NM: Optional[str] = None,
        LE_ORD_NM: Optional[str] = None,
        LE_CRSE_NM: Optional[str] = None,
    ) -> Any:
        params = self.__get_params(locals())
        return await self.get_acaInsTiInfo(params)

    async def elstimeTable(
        self,
        ATPT_OFCDC_SC_CODE: Optional[str] = None,
        SD_SCHUL_CODE: Optional[str] = None,
        AY: Optional[int] = None,
        SEM: Optional[int] = None,
        ALL_TI_YMD: Optional[int] = None,
        DGHT_CRSE_SC_NM: Optional[str] = None,
        ORD_SC_NM: Optional[str] = None,
        DDDEP_NM: Optional[str] = None,
        GRADE: Optional[int] = None,
        CLRM_NM: Optional[str] = None,
        CLASS_NM: Optional[str] = None,
        PERIO: Optional[int] = None,
        TI_FROM_YMD: Optional[int] = None,
        TI_TO_YMD: Optional[int] = None,
        SCHUL_CRSE_SC_NM: Optional[str] = None,
    ) -> Any:
        params = self.__get_params(locals())
        return await self.get_elstimeTable(params)

    async def mistimeTable(
        self,
        ATPT_OFCDC_SC_CODE: Optional[str] = None,
        SD_SCHUL_CODE: Optional[str] = None,
        AY: Optional[int] = None,
        SEM: Optional[int] = None,
        ALL_TI_YMD: Optional[int] = None,
        DGHT_CRSE_SC_NM: Optional[str] = None,
        ORD_SC_NM: Optional[str] = None,
        DDDEP_NM: Optional[str] = None,
        GRADE: Optional[int] = None,
        CLRM_NM: Optional[str] = None,
        CLASS_NM: Optional[str] = None,
        PERIO: Optional[int] = None,
        TI_FROM_YMD: Optional[int] = None,
        TI_TO_YMD: Optional[int] = None,
        SCHUL_CRSE_SC_NM: Optional[str] = None,
    ) -> Any:
        params = self.__get_params(locals())
        return await self.get_mistimeTable(params)

    async def histimeTable(
        self,
        ATPT_OFCDC_SC_CODE: Optional[str] = None,
        SD_SCHUL_CODE: Optional[str] = None,
        AY: Optional[int] = None,
        SEM: Optional[int] = None,
        ALL_TI_YMD: Optional[int] = None,
        DGHT_CRSE_SC_NM: Optional[str] = None,
        ORD_SC_NM: Optional[str] = None,
        DDDEP_NM: Optional[str] = None,
        GRADE: Optional[int] = None,
        CLRM_NM: Optional[str] = None,
        CLASS_NM: Optional[str] = None,
        PERIO: Optional[int] = None,
        TI_FROM_YMD: Optional[int] = None,
        TI_TO_YMD: Optional[int] = None,
        SCHUL_CRSE_SC_NM: Optional[str] = None,
    ) -> Any:
        params = self.__get_params(locals())
        return await self.get_histimeTable(params)

    async def spstimeTable(
        self,
        ATPT_OFCDC_SC_CODE: Optional[str] = None,
        SD_SCHUL_CODE: Optional[str] = None,
        AY: Optional[int] = None,
        SEM: Optional[int] = None,
        ALL_TI_YMD: Optional[int] = None,
        DGHT_CRSE_SC_NM: Optional[str] = None,
        ORD_SC_NM: Optional[str] = None,
        DDDEP_NM: Optional[str] = None,
        GRADE: Optional[int] = None,
        CLRM_NM: Optional[str] = None,
        CLASS_NM: Optional[str] = None,
        PERIO: Optional[int] = None,
        TI_FROM_YMD: Optional[int] = None,
        TI_TO_YMD: Optional[int] = None,
        SCHUL_CRSE_SC_NM: Optional[str] = None,
    ) -> Any:
        params = self.__get_params(locals())
        return await self.get_spstimeTable(params)

    async def classInfo(
        self,
        ATPT_OFCDC_SC_CODE: Optional[str] = None,
        SD_SCHUL_CODE: Optional[str] = None,
        AY: Optional[str] = None,
        GRADE: Optional[str] = None,
        DGHT_CRSE_SC_NM: Optional[str] = None,
        SCHUL_CRSE_SC_NM: Optional[str] = None,
        ORD_SC_NM: Optional[str] = None,
        DDDEP_NM: Optional[str] = None,
    ) -> Any:
        params = self.__get_params(locals())
        return await self.get_classInfo(params)

    async def schoolMajorinfo(
        self,
        ATPT_OFCDC_SC_CODE: Optional[str] = None,
        SD_SCHUL_CODE: Optional[str] = None,
        DGHT_CRSE_SC_NM: Optional[str] = None,
        ORD_SC_NM: Optional[str] = None,
    ) -> Any:
        params = self.__get_params(locals())
        return await self.get_schoolMajorinfo(params)

    async def schulAflcoinfo(
        self,
        ATPT_OFCDC_SC_CODE: Optional[str] = None,
        SD_SCHUL_CODE: Optional[str] = None,
        DGHT_CRSE_SC_NM: Optional[str] = None,
    ) -> Any:
        params = self.__get_params(locals())
        return await self.get_schulAflcoinfo(params)

    async def tiClrminfo(
        self,
        ATPT_OFCDC_SC_CODE: Optional[str] = None,
        SD_SCHUL_CODE: Optional[str] = None,
        AY: Optional[str] = None,
        GRADE: Optional[str] = None,
        SEM: Optional[str] = None,
        SCHUL_CRSE_SC_NM: Optional[str] = None,
        DGHT_CRSE_SC_NM: Optional[str] = None,
        ORD_SC_NM: Optional[str] = None,
        DDDEP_NM: Optional[str] = None,
    ) -> Any:
        params = self.__get_params(locals())
        return await self.get_tiClrminfo(params)
