from typing import Any, Optional

from aiohttp.client import ClientSession
from typing_extensions import Literal, Unpack

from neispy.domain import *
from neispy.params import *
from neispy.params.abc import AbstractRequestParams
from neispy.types import *

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
    ) -> Any: ...
    def get_schoolInfo(self, params: SchoolInfoParams) -> SchoolInfoDict: ...
    def get_mealServiceDietInfo(
        self, params: MealServiceDietInfoParams
    ) -> MealServiceDietInfoDict: ...
    def get_SchoolSchedule(
        self, params: SchoolScheduleParams
    ) -> SchoolScheduleDict: ...
    def get_acaInsTiInfo(self, params: AcaInsTiInfoParams) -> AcaInsTiInfoDict: ...
    def get_elsTimetable(self, params: TimetableParams) -> ElsTimeTableDict: ...
    def get_misTimetable(self, params: TimetableParams) -> MisTimeTableDict: ...
    def get_hisTimetable(self, params: TimetableParams) -> HisTimeTableDict: ...
    def get_spsTimetable(self, params: TimetableParams) -> SpsTimeTableDict: ...
    def get_elsTimetablebgs(self, params: TimetableParams) -> ElsTimeTableDict: ...
    def get_misTimetablebgs(self, params: TimetableParams) -> MisTimeTableDict: ...
    def get_hisTimetablebgs(self, params: TimetableParams) -> HisTimeTableDict: ...
    def get_spsTimetablebgs(self, params: TimetableParams) -> SpsTimeTableDict: ...
    def get_classInfo(self, params: ClassInfoParams) -> ClassInfoDict: ...
    def get_schoolMajorinfo(
        self, params: SchoolMajorInfoParams
    ) -> SchoolMajorInfoDict: ...
    def get_schulAflcoinfo(
        self, params: SchulAflcoInfoParams
    ) -> SchulAflcoInfoDict: ...
    def get_tiClrminfo(self, params: TiClrmInfoParams) -> TiClrmInfoDict: ...

class SyncNeispy(SyncNeispyRequest):
    def __init__(
        self,
        KEY: Optional[str] = None,
        Type: Literal["json", "xml"] = "json",
        pIndex: int = 1,
        pSize: int = 100,
        session: Optional[ClientSession] = None,
        only_rows: bool = True,
    ) -> None: ...
    def schoolInfo(
        self,
        **kwargs: Unpack[SchoolInfoParams],
    ) -> SchoolInfo: ...
    def mealServiceDietInfo(
        self,
        **kwargs: Unpack[MealServiceDietInfoParams],
    ) -> MealServiceDietInfo: ...
    def SchoolSchedule(
        self,
        **kwargs: Unpack[SchoolScheduleParams],
    ) -> SchoolSchedule: ...
    def acaInsTiInfo(
        self,
        **kwargs: Unpack[AcaInsTiInfoParams],
    ) -> AcaInsTiInfo: ...
    def elsTimetable(self, **kwargs: Unpack[TimetableParams]) -> ElsTimeTable: ...
    def misTimetable(self, **kwargs: Unpack[TimetableParams]) -> MisTimeTable: ...
    def hisTimetable(self, **kwargs: Unpack[TimetableParams]) -> HisTimeTable: ...
    def spsTimetable(self, **kwargs: Unpack[TimetableParams]) -> SpsTimeTable: ...
    def classInfo(
        self,
        **kwargs: Unpack[ClassInfoParams],
    ) -> ClassInfo: ...
    def schoolMajorinfo(
        self,
        **kwargs: Unpack[SchoolMajorInfoParams],
    ) -> SchoolMajorInfo: ...
    def schulAflcoinfo(
        self,
        **kwargs: Unpack[SchulAflcoInfoParams],
    ) -> SchulAflcoInfo: ...
    def tiClrminfo(
        self,
        **kwargs: Unpack[TiClrmInfoParams],
    ) -> TiClrmInfo: ...
