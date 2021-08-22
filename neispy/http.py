from types import TracebackType
from typing import Dict, Optional, Type, Union

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from aiohttp.client import ClientSession
from warnings import warn
from neispy.error import ExceptionsMapping


class NeispyRequest:
    BASE = "https://open.neis.go.kr/hub"

    def __init__(
        self,
        KEY: Optional[str],
        Type: Literal["json", "xml"],
        pIndex: int,
        pSize: int,
        session: Optional[ClientSession],
    ) -> None:
        self.KEY = KEY
        if not KEY:
            warn("API키가 없습니다, 샘플키로 요청합니다", UserWarning)

        self.pIndex = pIndex
        self.pSize = pSize
        self.Type = Type
        self.session = session

    async def request(
        self,
        method: str,
        endpoint: str,
        params: Dict[str, Union[str, int]],
    ):
        URL = self.BASE + endpoint

        if not self.session:
            self.session = ClientSession()

        async with self.session.request(method, URL, params=params) as response:
            data = await response.json(content_type=None)

            if result := data.get("RESULT"):
                code = result["CODE"]
                if code != "INFO-000":
                    msg = result["MESSAGE"]
                    raise ExceptionsMapping[result["CODE"]](code, msg)

            return data["row"]

    async def get_schoolInfo(self, params: Dict[str, Union[str, int]]):
        return await self.request("GET", "/schoolInfo", params)

    async def get_mealServiceDietInfo(self, params: Dict[str, Union[str, int]]):
        return await self.request("GET", "/mealServiceDietInfo", params)

    async def get_SchoolSchedule(self, params: Dict[str, Union[str, int]]):
        return await self.request("GET", "/schoolSchedule", params)

    async def get_acaInsTiInfo(self, params: Dict[str, Union[str, int]]):
        return await self.request("GET", "/acaInsTiInfo", params)

    async def get_elstimeTable(self, params: Dict[str, Union[str, int]]):
        return await self.request("GET", "/elstimeTable", params)

    async def get_mistimeTable(self, params: Dict[str, Union[str, int]]):
        return await self.request("GET", "/mistimeTable", params)

    async def get_histimeTable(self, params: Dict[str, Union[str, int]]):
        return await self.request("GET", "/histimeTable", params)

    async def get_spstimeTable(self, params: Dict[str, Union[str, int]]):
        return await self.request("GET", "/spstimeTable", params)

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
