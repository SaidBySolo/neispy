from typing import Any, Dict, Optional, Union

from aiohttp.client import ClientSession
from typing_extensions import Literal, Unpack

from neispy.params import *
from neispy.params.abc import AbstractRequestParams


class SyncNeispyRequest:
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
        self.pIndex = pIndex
        self.pSize = pSize
        self.Type = Type
        self.session = session
        self.only_rows = only_rows

    def request(
        self,
        method: str,
        endpoint: str,
        params: AbstractRequestParams,
    ):
        ...

    def get_schoolInfo(self, params: SchoolInfoParams):
        ...

    def get_mealServiceDietInfo(self, params: MealServiceDietInfoParams):
        ...

    def get_SchoolSchedule(self, params: SchoolScheduleParams):
        ...

    def get_acaInsTiInfo(self, params: AcaInsTiInfoParams):
        ...

    def get_elsTimetable(self, params: TimetableParams):
        ...

    def get_misTimetable(self, params: TimetableParams):
        ...

    def get_hisTimetable(self, params: TimetableParams):
        ...

    def get_spsTimetable(self, params: TimetableParams):
        ...

    def get_elsTimetablebgs(self, params: TimetableParams):
        ...

    def get_misTimetablebgs(self, params: TimetableParams):
        ...

    def get_hisTimetablebgs(self, params: TimetableParams):
        ...

    def get_spsTimetablebgs(self, params: TimetableParams):
        ...

    def get_classInfo(self, params: ClassInfoParams):
        ...

    def get_schoolMajorinfo(self, params: SchoolMajorInfoParams):
        ...

    def get_schulAflcoinfo(self, params: SchulAflcoInfoParams):
        ...

    def get_tiClrminfo(self, params: TiClrmInfoParams):
        ...


class SyncNeispy(SyncNeispyRequest):
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

    def schoolInfo(
        self,
        **kwargs: Unpack[SchoolInfoParams],
    ) -> Any:
        ...

    def mealServiceDietInfo(
        self,
        **kwargs: Unpack[MealServiceDietInfoParams],
    ) -> Any:
        ...

    def SchoolSchedule(
        self,
        **kwargs: Unpack[SchoolScheduleParams],
    ) -> Any:
        ...

    def acaInsTiInfo(
        self,
        **kwargs: Unpack[AcaInsTiInfoParams],
    ) -> Any:
        ...

    def elsTimetable(self, **kwargs: Unpack[TimetableParams]) -> Any:
        ...

    def misTimetable(self, **kwargs: Unpack[TimetableParams]) -> Any:
        ...

    def hisTimetable(self, **kwargs: Unpack[TimetableParams]) -> Any:
        ...

    def spsTimetable(self, **kwargs: Unpack[TimetableParams]) -> Any:
        ...

    def classInfo(
        self,
        **kwargs: Unpack[ClassInfoParams],
    ) -> Any:
        ...

    def schoolMajorinfo(
        self,
        **kwargs: Unpack[SchoolMajorInfoParams],
    ) -> Any:
        ...

    def schulAflcoinfo(
        self,
        **kwargs: Unpack[SchulAflcoInfoParams],
    ) -> Any:
        ...

    def tiClrminfo(
        self,
        **kwargs: Unpack[TiClrmInfoParams],
    ) -> Any:
        ...
