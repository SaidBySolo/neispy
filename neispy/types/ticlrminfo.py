from typing_extensions import TypedDict

from neispy.types.base import NeisDict, SchoolRelatedBaseDict


class TiClrmInfoRowDict(SchoolRelatedBaseDict):
    AY: str
    "학년도"
    GRADE: str
    "학년"
    SEM: str
    "학기"
    SCHUL_CRSE_SC_NM: str
    "학교과정명"
    DGHT_CRSE_SC_NM: str
    "주야과정명"
    ORD_SC_NM: str
    "계열명"
    DDDEP_NM: str
    "학과명"
    CLRM_NM: str
    "강의실명"
    LOAD_DTM: str
    "수정일"


class TiClrmInfoDict(TypedDict):
    tiClrminfo: NeisDict[TiClrmInfoRowDict]
