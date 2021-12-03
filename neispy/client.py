try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal
from json import loads, dumps
from types import SimpleNamespace
from neispy.http import NeispyRequest
from typing import Any, Callable, Coroutine, Dict, Optional, TypeVar, cast
from aiohttp.client import ClientSession
from asyncio.events import get_event_loop

from neispy.sync import SyncNeispy
from functools import wraps

# KST = datetime.timezone(datetime.timedelta(hours=9))


# def now() -> Any:
#     return datetime.datetime.now(tz=KST).strftime("%Y%m%d")


CORO = TypeVar("CORO", bound=Callable[..., Coroutine[Any, Any, Any]])


def to_obj(func: CORO) -> CORO:
    @wraps(func)
    async def inner(*args: Any, **kwargs: Any) -> Any:
        data = await func(*args, **kwargs)
        return loads(dumps(data), object_hook=lambda d: SimpleNamespace(**d))

    return cast(CORO, inner)


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
        neispy = cls(KEY, Type, pIndex, pSize, only_rows=only_rows)
        origin_request_func = getattr(neispy, "request")

        # Remove some methods
        setattr(neispy, "__aenter__", None)
        setattr(neispy, "__aexit__", None)
        setattr(neispy, "sync", None)
        del neispy.__aenter__
        del neispy.__aexit__
        del neispy.sync

        async def close_session_request(*args: Any, **kwargs: Any) -> Any:
            try:
                if neispy.session and neispy.session.closed or not neispy.session:
                    neispy.session = ClientSession()
                return await origin_request_func(*args, **kwargs)
            finally:
                if neispy.session:
                    await neispy.session.close()

        def to_sync_func(func: Any):
            def wrapper(*args: Any, **kwargs: Any):
                loop = get_event_loop()

                if loop.is_running():
                    return func(*args, **kwargs)

                return loop.run_until_complete(func(*args, **kwargs))

            return wrapper

        method_list = [
            func
            for func in dir(neispy)
            if callable(getattr(neispy, func))
            and not func.startswith("__")
            and not func.startswith("_")
        ]

        neispy.__setattr__("request", close_session_request)

        for method in method_list:
            neispy.__setattr__(method, to_sync_func(getattr(neispy, method)))

        return cast(SyncNeispy, neispy)

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
        return await self.get_elsTimetable(params)

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
        return await self.get_misTimetable(params)

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
        return await self.get_hisTimetable(params)

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
        return await self.get_spsTimetable(params)

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
