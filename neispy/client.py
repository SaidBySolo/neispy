from typing import Any, Optional, cast

from aiohttp.client import ClientSession
from typing_extensions import Unpack


from neispy.http import NeispyRequest
from neispy.params import *
from neispy.sync import SyncNeispy
from neispy.domain import *


def is_legacy_timetable(
    params: TimetableParams,
) -> bool:
    check_params = ("AY", "ALL_TI_YMD", "TI_FROM_YMD", "TI_TO_YMD")
    for param in check_params:
        if p := params.get(param):
            if int(p) < 2023:
                return True

            if int(str(p)[:4]) < 2023:
                return True
    return False


class Neispy(NeispyRequest):
    def __init__(
        self,
        KEY: Optional[str] = None,
        pIndex: int = 1,
        pSize: int = 100,
        session: Optional[ClientSession] = None,
    ) -> None:
        super().__init__(
            KEY=KEY,
            pIndex=pIndex,
            pSize=pSize,
            session=session,
        )

    @classmethod
    def sync(
        cls,
        KEY: Optional[str] = None,
        pIndex: int = 1,
        pSize: int = 100,
    ) -> SyncNeispy:
        return cast(SyncNeispy, super().sync(KEY, pIndex, pSize))

    async def schoolInfo(
        self,
        **kwargs: Unpack[SchoolInfoParams],
    ) -> SchoolInfo:
        r = await self.get_schoolInfo(kwargs)
        return SchoolInfo.from_dict(r)

    async def mealServiceDietInfo(
        self,
        **kwargs: Unpack[MealServiceDietInfoParams],
    ) -> Any:
        r = await self.get_mealServiceDietInfo(kwargs)
        return MealServiceDietInfo.from_dict(r)

    async def SchoolSchedule(
        self,
        **kwargs: Unpack[SchoolScheduleParams],
    ) -> Any:
        r = await self.get_SchoolSchedule(kwargs)
        return SchoolSchedule.from_dict(r)

    async def acaInsTiInfo(
        self,
        **kwargs: Unpack[AcaInsTiInfoParams],
    ) -> Any:
        return await self.get_acaInsTiInfo(kwargs)

    async def elsTimetable(self, **kwargs: Unpack[TimetableParams]) -> Any:
        return await (
            self.get_elsTimetablebgs(kwargs)
            if is_legacy_timetable(kwargs)
            else self.get_elsTimetable(kwargs)
        )

    async def misTimetable(self, **kwargs: Unpack[TimetableParams]) -> Any:
        return await (
            self.get_misTimetablebgs(kwargs)
            if is_legacy_timetable(kwargs)
            else self.get_misTimetable(kwargs)
        )

    async def hisTimetable(self, **kwargs: Unpack[TimetableParams]) -> Any:
        return await (
            self.get_hisTimetablebgs(kwargs)
            if is_legacy_timetable(kwargs)
            else self.get_hisTimetable(kwargs)
        )

    async def spsTimetable(self, **kwargs: Unpack[TimetableParams]) -> Any:
        return await (
            self.get_spsTimetablebgs(kwargs)
            if is_legacy_timetable(kwargs)
            else self.get_spsTimetable(kwargs)
        )

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
