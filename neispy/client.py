from typing import Any, Optional, cast

from aiohttp.client import ClientSession
from typing_extensions import Literal, Unpack

from neispy.http import NeispyRequest
from neispy.params import *
from neispy.sync import SyncNeispy


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

    async def schoolInfo(
        self,
        **kwargs: Unpack[SchoolInfoParams],
    ) -> Any:
        return await self.get_schoolInfo(kwargs)

    async def mealServiceDietInfo(
        self,
        **kwargs: Unpack[MealServiceDietInfoParams],
    ) -> Any:
        return await self.get_mealServiceDietInfo(kwargs)

    async def SchoolSchedule(
        self,
        **kwargs: Unpack[SchoolScheduleParams],
    ) -> Any:
        return await self.get_SchoolSchedule(kwargs)

    async def acaInsTiInfo(
        self,
        **kwargs: Unpack[AcaInsTiInfoParams],
    ) -> Any:
        return await self.get_acaInsTiInfo(kwargs)

    async def elsTimetable(self, **kwargs: Unpack[TimetableParams]) -> Any:
        return await self.get_elsTimetable(kwargs)

    async def misTimetable(self, **kwargs: Unpack[TimetableParams]) -> Any:
        return await self.get_misTimetable(kwargs)

    async def hisTimetable(self, **kwargs: Unpack[TimetableParams]) -> Any:
        return await self.get_hisTimetable(kwargs)

    async def spsTimetable(self, **kwargs: Unpack[TimetableParams]) -> Any:
        return await self.get_spsTimetable(kwargs)

    async def classInfo(
        self,
        **kwargs: Unpack[ClassInfoParams],
    ) -> Any:
        return await self.get_classInfo(kwargs)

    async def schoolMajorinfo(
        self,
        **kwargs: Unpack[SchoolMajorInfoParams],
    ) -> Any:
        return await self.get_schoolMajorinfo(kwargs)

    async def schulAflcoinfo(
        self,
        **kwargs: Unpack[SchulAflcoInfoParams],
    ) -> Any:
        return await self.get_schulAflcoinfo(kwargs)

    async def tiClrminfo(
        self,
        **kwargs: Unpack[TiClrmInfoParams],
    ) -> Any:
        return await self.get_tiClrminfo(kwargs)
