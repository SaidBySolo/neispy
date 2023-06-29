try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from functools import wraps
from json import dumps, loads
from types import SimpleNamespace
from typing import Any, Callable, Coroutine, Dict, Optional, TypeVar, cast

from aiohttp.client import ClientSession

from neispy.http import NeispyRequest
from neispy.sync import SyncNeispy


CORO = TypeVar("CORO", bound=Callable[..., Coroutine[Any, Any, Any]])


def to_obj(func: CORO) -> CORO:
    @wraps(func)
    async def inner(*args: Any, **kwargs: Any) -> Any:
        data = await func(*args, **kwargs)
        return loads(dumps(data), object_hook=lambda d: SimpleNamespace(**d))

    return cast(CORO, inner)


def is_legacy_timetable(
    params: Dict[str, Any],
) -> bool:
    return (
        (params["AY"] and params["AY"] < 2023)
        or (params["ALL_TI_YMD"] and int(str(params["ALL_TI_YMD"])[:4]) < 2023)
        or (params["TI_FROM_YMD"] and int(str(params["TI_FROM_YMD"])[:4]) < 2023)
        or (params["TI_TO_YMD"] and int(str(params["TI_TO_YMD"])[:4]) < 2023)
    )


class Neispy(NeispyRequest):
    def __init__(
        self,
        KEY: Optional[str] = None,
        Type: Literal["json", "xml"] = "json",
        pIndex: int = 1,
        pSize: int = 100,
        session: Optional[ClientSession] = None,
        only_rows: bool = True,
    ) -> None:
        super().__init__(
            KEY=KEY,
            Type=Type,
            pIndex=pIndex,
            pSize=pSize,
            session=session,
            only_rows=only_rows,
        )

    def __get_params(self, locals: Dict[str, Any]) -> Any:
        locals.pop("self")
        return {k: v for k, v in locals.items() if v is not None}

    @classmethod
    def sync(
        cls,
        KEY: Optional[str] = None,
        Type: Literal["json", "xml"] = "json",
        pIndex: int = 1,
        pSize: int = 100,
        only_rows: bool = True,
    ) -> SyncNeispy:
        return cast(
            SyncNeispy, super().sync(KEY, Type, pIndex, pSize, only_rows=only_rows)
        )

    @to_obj
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

    @to_obj
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

    @to_obj
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

    @to_obj
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

    @to_obj
    async def elsTimetable(
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
        return await (
            self.get_elsTimetablebgs(params)
            if is_legacy_timetable(params)
            else self.get_elsTimetable(params)
        )

    @to_obj
    async def misTimetable(
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
        return await (
            self.get_misTimetablebgs(params)
            if is_legacy_timetable(params)
            else self.get_misTimetable(params)
        )

    @to_obj
    async def hisTimetable(
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
        return await (
            self.get_hisTimetablebgs(params)
            if is_legacy_timetable(params)
            else self.get_hisTimetable(params)
        )

    @to_obj
    async def spsTimetable(
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
        return await (
            self.get_spsTimetablebgs(params)
            if is_legacy_timetable(params)
            else self.get_spsTimetable(params)
        )

    @to_obj
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

    @to_obj
    async def schoolMajorinfo(
        self,
        ATPT_OFCDC_SC_CODE: Optional[str] = None,
        SD_SCHUL_CODE: Optional[str] = None,
        DGHT_CRSE_SC_NM: Optional[str] = None,
        ORD_SC_NM: Optional[str] = None,
    ) -> Any:
        params = self.__get_params(locals())
        return await self.get_schoolMajorinfo(params)

    @to_obj
    async def schulAflcoinfo(
        self,
        ATPT_OFCDC_SC_CODE: Optional[str] = None,
        SD_SCHUL_CODE: Optional[str] = None,
        DGHT_CRSE_SC_NM: Optional[str] = None,
    ) -> Any:
        params = self.__get_params(locals())
        return await self.get_schulAflcoinfo(params)

    @to_obj
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
