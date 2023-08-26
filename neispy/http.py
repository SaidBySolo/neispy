from asyncio import get_event_loop
from types import TracebackType
from typing import TYPE_CHECKING, Any, Dict, NoReturn, Optional, Type, Union, cast
from warnings import warn

from aiohttp.client import ClientSession
from typing_extensions import Self

from neispy.error import ExceptionsMapping
from neispy.params import *
from neispy.params.abc import AbstractNotRequiredRequestParams, AbstractRequestParams
from neispy.types import *

if TYPE_CHECKING:
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
    ) -> "SyncNeispyRequest":
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

        def to_sync_func(func: Any) -> Any:
            def wrapper(*args: Any, **kwargs: Any) -> Any:
                if loop.is_running():
                    return func(*args, **kwargs)

                return loop.run_until_complete(func(*args, **kwargs))

            return wrapper

        def dont_use_sync(*args: Any, **kwargs: Any) -> NoReturn:
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
        return cast("SyncNeispyRequest", http)

    async def request(
        self,
        method: str,
        endpoint: str,
        params: Union[AbstractRequestParams, AbstractNotRequiredRequestParams],
    ) -> Any:
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
        r: SchoolInfoDict = await self.request("GET", "/schoolInfo", params)
        return r

    async def get_mealServiceDietInfo(
        self, params: MealServiceDietInfoParams
    ) -> MealServiceDietInfoDict:
        r: MealServiceDietInfoDict = await self.request(
            "GET", "/mealServiceDietInfo", params
        )
        return r

    async def get_SchoolSchedule(
        self, params: SchoolScheduleParams
    ) -> SchoolScheduleDict:
        r: SchoolScheduleDict = await self.request("GET", "/SchoolSchedule", params)
        return r

    async def get_acaInsTiInfo(self, params: AcaInsTiInfoParams) -> AcaInsTiInfoDict:
        r: AcaInsTiInfoDict = await self.request("GET", "/acaInsTiInfo", params)
        return r

    async def get_elsTimetable(self, params: TimetableParams) -> ElsTimeTableDict:
        r: ElsTimeTableDict = await self.request("GET", "/elsTimetable", params)
        return r

    async def get_misTimetable(self, params: TimetableParams) -> MisTimeTableDict:
        r: MisTimeTableDict = await self.request("GET", "/misTimetable", params)
        return r

    async def get_hisTimetable(self, params: TimetableParams) -> HisTimeTableDict:
        r: HisTimeTableDict = await self.request("GET", "/hisTimetable", params)
        return r

    async def get_spsTimetable(self, params: TimetableParams) -> SpsTimeTableDict:
        r: SpsTimeTableDict = await self.request("GET", "/spsTimetable", params)
        return r

    async def get_elsTimetablebgs(self, params: TimetableParams) -> ElsTimeTableDict:
        r: ElsTimeTableDict = await self.request("GET", "/elsTimetablebgs", params)
        return r

    async def get_misTimetablebgs(self, params: TimetableParams) -> MisTimeTableDict:
        r: MisTimeTableDict = await self.request("GET", "/misTimetablebgs", params)
        return r

    async def get_hisTimetablebgs(self, params: TimetableParams) -> HisTimeTableDict:
        r: HisTimeTableDict = await self.request("GET", "/hisTimetablebgs", params)
        return r

    async def get_spsTimetablebgs(self, params: TimetableParams) -> SpsTimeTableDict:
        r: SpsTimeTableDict = await self.request("GET", "/spsTimetablebgs", params)
        return r

    async def get_classInfo(self, params: ClassInfoParams) -> ClassInfoDict:
        r: ClassInfoDict = await self.request("GET", "/classInfo", params)
        return r

    async def get_schoolMajorinfo(
        self, params: SchoolMajorInfoParams
    ) -> SchoolMajorInfoDict:
        r: SchoolMajorInfoDict = await self.request("GET", "/schoolMajorinfo", params)
        return r

    async def get_schulAflcoinfo(
        self, params: SchulAflcoInfoParams
    ) -> SchulAflcoInfoDict:
        r: SchulAflcoInfoDict = await self.request("GET", "/schulAflcoinfo", params)
        return r

    async def get_tiClrminfo(self, params: TiClrmInfoParams) -> TiClrmInfoDict:
        r: TiClrmInfoDict = await self.request("GET", "/tiClrminfo", params)
        return r

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None:
        if self.session and not self.session.closed:
            await self.session.close()
