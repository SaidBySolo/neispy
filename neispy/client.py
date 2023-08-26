from typing import TYPE_CHECKING, Any, Optional, cast

from aiohttp.client import ClientSession
from typing_extensions import Unpack

from neispy.domain import *
from neispy.http import NeispyRequest
from neispy.params import *

if TYPE_CHECKING:
    from neispy.sync import SyncNeispy


def is_legacy_timetable(
    params: TimetableParams,
) -> bool:
    check_params = ("AY", "ALL_TI_YMD", "TI_FROM_YMD", "TI_TO_YMD")
    for param in check_params:
        p = params.get(param)
        if p:
            p = cast(str, p)
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
    ) -> "SyncNeispy":
        return cast("SyncNeispy", super().sync(KEY, pIndex, pSize))

    async def schoolInfo(
        self,
        **kwargs: Unpack[SchoolInfoParams],
    ) -> SchoolInfo:
        r = await self.get_schoolInfo(kwargs)
        return SchoolInfo.from_dict(r)

    async def mealServiceDietInfo(
        self,
        **kwargs: Unpack[MealServiceDietInfoParams],
    ) -> MealServiceDietInfo:
        r = await self.get_mealServiceDietInfo(kwargs)
        return MealServiceDietInfo.from_dict(r)

    async def SchoolSchedule(
        self,
        **kwargs: Unpack[SchoolScheduleParams],
    ) -> SchoolSchedule:
        r = await self.get_SchoolSchedule(kwargs)
        return SchoolSchedule.from_dict(r)

    async def acaInsTiInfo(
        self,
        **kwargs: Unpack[AcaInsTiInfoParams],
    ) -> AcaInsTiInfo:
        r = await self.get_acaInsTiInfo(kwargs)
        return AcaInsTiInfo.from_dict(r)

    async def elsTimetable(self, **kwargs: Unpack[TimetableParams]) -> ElsTimeTable:
        r = await (
            self.get_elsTimetablebgs(kwargs)
            if is_legacy_timetable(kwargs)
            else self.get_elsTimetable(kwargs)
        )
        return ElsTimeTable.from_dict(r)

    async def misTimetable(self, **kwargs: Unpack[TimetableParams]) -> MisTimeTable:
        r = await (
            self.get_misTimetablebgs(kwargs)
            if is_legacy_timetable(kwargs)
            else self.get_misTimetable(kwargs)
        )
        return MisTimeTable.from_dict(r)

    async def hisTimetable(self, **kwargs: Unpack[TimetableParams]) -> HisTimeTable:
        r = await (
            self.get_hisTimetablebgs(kwargs)
            if is_legacy_timetable(kwargs)
            else self.get_hisTimetable(kwargs)
        )
        return HisTimeTable.from_dict(r)

    async def spsTimetable(self, **kwargs: Unpack[TimetableParams]) -> Any:
        r = await (
            self.get_spsTimetablebgs(kwargs)
            if is_legacy_timetable(kwargs)
            else self.get_spsTimetable(kwargs)
        )
        return SpsTimeTable.from_dict(r)

    async def classInfo(
        self,
        **kwargs: Unpack[ClassInfoParams],
    ) -> ClassInfo:
        r = await self.get_classInfo(kwargs)
        return ClassInfo.from_dict(r)

    async def schoolMajorinfo(
        self,
        **kwargs: Unpack[SchoolMajorInfoParams],
    ) -> SchoolMajorInfo:
        r = await self.get_schoolMajorinfo(kwargs)
        return SchoolMajorInfo.from_dict(r)

    async def schulAflcoinfo(
        self,
        **kwargs: Unpack[SchulAflcoInfoParams],
    ) -> SchulAflcoInfo:
        r = await self.get_schulAflcoinfo(kwargs)
        return SchulAflcoInfo.from_dict(r)

    async def tiClrminfo(
        self,
        **kwargs: Unpack[TiClrmInfoParams],
    ) -> Any:
        r = await self.get_tiClrminfo(kwargs)
        return TiClrmInfo.from_dict(r)
