from asyncio import get_event_loop
from types import TracebackType
from typing import Any, Dict, Optional, Type, cast
from warnings import warn

from aiohttp.client import ClientSession

from neispy.error import ExceptionsMapping
from neispy.params import *
from neispy.params.abc import AbstractRequestParams
from neispy.types import *
from neispy.sync import SyncNeispyRequest


class NeispyRequest:
    BASE = "https://open.neis.go.kr/hub"

    def __init__(
        self,
        KEY: Optional[str],
        pIndex: int,
        pSize: int,
        session: Optional[ClientSession],
    ) -> None:
        self.KEY = KEY
        if not KEY:
            warn("API키가 없습니다, 샘플키로 요청합니다", UserWarning)

        self.pIndex = pIndex
        self.pSize = pSize
        self.session = session

        self.__default_params: Dict[str, Any] = {
            "pIndex": self.pIndex,
            "pSize": self.pSize,
            "type": "json",
        }

        if self.KEY:
            self.__default_params["KEY"] = self.KEY

    @classmethod
    def sync(
        cls,
        KEY: Optional[str],
        pIndex: int,
        pSize: int,
    ) -> SyncNeispyRequest:
        http = cls(KEY, pIndex, pSize, None)
        origin_request_func = getattr(http, "request")
        loop = get_event_loop()

        # Remove some methods
        setattr(http, "__aenter__", None)
        setattr(http, "__aexit__", None)

        del http.__aenter__
        del http.__aexit__

        async def close_session_request(*args: Any, **kwargs: Any) -> Any:
            try:
                if http.session and http.session.closed or not http.session:
                    http.session = ClientSession()
                return await origin_request_func(*args, **kwargs)
            finally:
                if http.session:
                    await http.session.close()

        def to_sync_func(func: Any):
            def wrapper(*args: Any, **kwargs: Any):
                if loop.is_running():
                    return func(*args, **kwargs)

                return loop.run_until_complete(func(*args, **kwargs))

            return wrapper

        def dont_use_sync(*args: Any, **kwargs: Any):
            raise AttributeError("Already synced")

        method_list = [
            func
            for func in dir(http)
            if callable(getattr(http, func))
            and not func.startswith("__")
            and not func.startswith("_")
        ]

        http.__setattr__("request", close_session_request)

        for method in method_list:
            http.__setattr__(method, to_sync_func(getattr(http, method)))

        setattr(http.__class__, "sync", property(dont_use_sync))
        return cast(SyncNeispyRequest, http)

    async def request(
        self,
        method: str,
        endpoint: str,
        params: AbstractRequestParams,
    ):
        URL = self.BASE + endpoint

        if not self.session:
            self.session = ClientSession()

        async with self.session.request(
            method, URL, params={**self.__default_params, **params}
        ) as response:
            data = await response.json(content_type=None)

            if data.get("RESULT"):
                result = data["RESULT"]
                code = result["CODE"]
                if code != "INFO-000":
                    msg = result["MESSAGE"]
                    raise ExceptionsMapping[result["CODE"]](code, msg)

            return data

    async def get_schoolInfo(self, params: SchoolInfoParams) -> SchoolInfoDict:
        return await self.request("GET", "/schoolInfo", params)

    async def get_mealServiceDietInfo(
        self, params: MealServiceDietInfoParams
    ) -> MealServiceDietInfoDict:
        return await self.request("GET", "/mealServiceDietInfo", params)

    async def get_SchoolSchedule(self, params: SchoolScheduleParams):
        return await self.request("GET", "/SchoolSchedule", params)

    async def get_acaInsTiInfo(self, params: AcaInsTiInfoParams):
        return await self.request("GET", "/acaInsTiInfo", params)

    async def get_elsTimetable(self, params: TimetableParams):
        return await self.request("GET", "/elsTimetable", params)

    async def get_misTimetable(self, params: TimetableParams):
        return await self.request("GET", "/misTimetable", params)

    async def get_hisTimetable(self, params: TimetableParams):
        return await self.request("GET", "/hisTimetable", params)

    async def get_spsTimetable(self, params: TimetableParams):
        return await self.request("GET", "/spsTimetable", params)

    async def get_classInfo(self, params: ClassInfoParams):
        return await self.request("GET", "/classInfo", params)

    async def get_schoolMajorinfo(self, params: SchoolMajorInfoParams):
        return await self.request("GET", "/schoolMajorinfo", params)

    async def get_schulAflcoinfo(self, params: SchulAflcoInfoParams):
        return await self.request("GET", "/schulAflcoinfo", params)

    async def get_tiClrminfo(self, params: TiClrmInfoParams):
        return await self.request("GET", "/tiClrminfo", params)

    async def __aenter__(self):
        return self

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ):
        if self.session and not self.session.closed:
            await self.session.close()
