from typing import Any, Dict, Optional, Union

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from aiohttp.client import ClientSession


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

    def _default_params(self) -> Dict[str, Union[str, int]]:
        ...

    def __loads(self, data: Any):
        ...

    def request(
        self,
        method: str,
        endpoint: str,
        params: Dict[str, Union[str, int]],
    ):
        ...

    def get_schoolInfo(self, params: Dict[str, Union[str, int]]):
        ...

    def get_mealServiceDietInfo(self, params: Dict[str, Union[str, int]]):
        ...

    def get_SchoolSchedule(self, params: Dict[str, Union[str, int]]):
        ...

    def get_acaInsTiInfo(self, params: Dict[str, Union[str, int]]):
        ...

    def get_elsTimetable(self, params: Dict[str, Union[str, int]]):
        ...

    def get_misTimetable(self, params: Dict[str, Union[str, int]]):
        ...

    def get_hisTimetable(self, params: Dict[str, Union[str, int]]):
        ...

    def get_spsTimetable(self, params: Dict[str, Union[str, int]]):
        ...

    def get_classInfo(self, params: Dict[str, Union[str, int]]):
        ...

    def get_schoolMajorinfo(self, params: Dict[str, Union[str, int]]):
        ...

    def get_schulAflcoinfo(self, params: Dict[str, Union[str, int]]):
        ...

    def get_tiClrminfo(self, params: Dict[str, Union[str, int]]):
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

    def __get_params(self, locals: Dict[str, Any]) -> Any:
        ...

    def schoolInfo(
        self,
        ATPT_OFCDC_SC_CODE: Optional[str] = None,
        SD_SCHUL_CODE: Optional[str] = None,
        SCHUL_NM: Optional[str] = None,
        SCHUL_KND_SC_NM: Optional[str] = None,
        LCTN_SC_NM: Optional[str] = None,
        FOND_SC_NM: Optional[str] = None,
    ) -> Any:
        ...

    def mealServiceDietInfo(
        self,
        ATPT_OFCDC_SC_CODE: Optional[str] = None,
        SD_SCHUL_CODE: Optional[str] = None,
        MMEAL_SC_CODE: Optional[str] = None,
        MLSV_YMD: Optional[str] = None,
        MLSV_FROM_YMD: Optional[str] = None,
        MLSV_TO_YMD: Optional[str] = None,
    ) -> Any:
        ...

    def SchoolSchedule(
        self,
        ATPT_OFCDC_SC_CODE: Optional[str] = None,
        SD_SCHUL_CODE: Optional[str] = None,
        DGHT_CRSE_SC_NM: Optional[str] = None,
        SCHUL_CRSE_SC_NM: Optional[str] = None,
        AA_YMD: Optional[int] = None,
        AA_FROM_YMD: Optional[int] = None,
        AA_TO_YMD: Optional[int] = None,
    ) -> Any:
        ...

    def acaInsTiInfo(
        self,
        ATPT_OFCDC_SC_CODE: Optional[str] = None,
        ADMST_ZONE_NM: Optional[str] = None,
        ACA_ASNUM: Optional[str] = None,
        REALM_SC_NM: Optional[str] = None,
        LE_ORD_NM: Optional[str] = None,
        LE_CRSE_NM: Optional[str] = None,
    ) -> Any:
        ...

    def elsTimetable(
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
        ...

    def misTimetable(
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
        ...

    def hisTimetable(
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
        ...

    def spsTimetable(
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
        ...

    def classInfo(
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
        ...

    def schoolMajorinfo(
        self,
        ATPT_OFCDC_SC_CODE: Optional[str] = None,
        SD_SCHUL_CODE: Optional[str] = None,
        DGHT_CRSE_SC_NM: Optional[str] = None,
        ORD_SC_NM: Optional[str] = None,
    ) -> Any:
        ...

    def schulAflcoinfo(
        self,
        ATPT_OFCDC_SC_CODE: Optional[str] = None,
        SD_SCHUL_CODE: Optional[str] = None,
        DGHT_CRSE_SC_NM: Optional[str] = None,
    ) -> Any:
        ...

    def tiClrminfo(
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
        ...
