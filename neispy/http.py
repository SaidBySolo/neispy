from types import TracebackType
from typing import Any, Dict, Optional, Type, Union

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from aiohttp.client import ClientSession
from warnings import warn
from neispy.error import ExceptionsMapping
from types import SimpleNamespace
from json import loads


class NeispyRequest:
    BASE = "https://open.neis.go.kr/hub"

    def __init__(
        self,
        KEY: Optional[str],
        Type: Literal["json", "xml"],
        pIndex: int,
        pSize: int,
        session: Optional[ClientSession],
        only_rows: bool = True,
    ) -> None:
        self.KEY = KEY
        if not KEY:
            warn("API키가 없습니다, 샘플키로 요청합니다", UserWarning)

        self.pIndex = pIndex
        self.pSize = pSize
        self.Type = Type
        self.session = session
        self.only_rows = only_rows

    def _default_params(self) -> Dict[str, Union[str, int]]:
        default_params = {
            "pIndex": self.pIndex,
            "pSize": self.pSize,
            "type": self.Type,
        }

        if self.KEY:
            default_params["KEY"] = self.KEY

        return default_params

    def __loads(self, data: Any):
        return loads(data, object_hook=lambda d: SimpleNamespace(**d))

    async def request(
        self,
        method: str,
        endpoint: str,
        params: Dict[str, Union[str, int]],
    ):
        URL = self.BASE + endpoint

        if not self.session:
            self.session = ClientSession()

        default_params = self._default_params()
        default_params.update(params)

        async with self.session.request(method, URL, params=default_params) as response:
            data = await response.json(content_type=None, loads=self.__loads)

            if getattr(data, "RESULT", None):
                result = data.RESULT
                code = result.CODE
                if code != "INFO-000":
                    msg = result.MESSAGE
                    raise ExceptionsMapping[result.CODE](code, msg)

            if self.only_rows:
                return list(data.__dict__.values())[0][1].row

            return data

    async def get_schoolInfo(self, params: Dict[str, Union[str, int]]):
        return await self.request("GET", "/schoolInfo", params)

    async def get_mealServiceDietInfo(self, params: Dict[str, Union[str, int]]):
        return await self.request("GET", "/mealServiceDietInfo", params)

    async def get_SchoolSchedule(self, params: Dict[str, Union[str, int]]):
        return await self.request("GET", "/SchoolSchedule", params)

    async def get_acaInsTiInfo(self, params: Dict[str, Union[str, int]]):
        return await self.request("GET", "/acaInsTiInfo", params)

    async def get_elsTimetable(self, params: Dict[str, Union[str, int]]):
        return await self.request("GET", "/elsTimetable", params)

    async def get_misTimetable(self, params: Dict[str, Union[str, int]]):
        return await self.request("GET", "/misTimetable", params)

    async def get_hisTimetable(self, params: Dict[str, Union[str, int]]):
        return await self.request("GET", "/hisTimetable", params)

    async def get_spsTimetable(self, params: Dict[str, Union[str, int]]):
        return await self.request("GET", "/spsTimetable", params)

    async def get_classInfo(self, params: Dict[str, Union[str, int]]):
        return await self.request("GET", "/classInfo", params)

    async def get_schoolMajorinfo(self, params: Dict[str, Union[str, int]]):
        return await self.request("GET", "/schoolMajorinfo", params)

    async def get_schulAflcoinfo(self, params: Dict[str, Union[str, int]]):
        return await self.request("GET", "/schulAflcoinfo", params)

    async def get_tiClrminfo(self, params: Dict[str, Union[str, int]]):
        return await self.request("GET", "/tiClrminfo", params)

    async def __aenter__(self):
        return self

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ):
        if self.session:
            await self.session.close()
