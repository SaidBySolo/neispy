from typing_extensions import TypedDict

from neispy.types.base import NeisDict, SchoolRelatedBaseDict


class HisTimeTableRowDict(SchoolRelatedBaseDict):
    AY: str
    "학년도"
    SEM: str
    "학기"
    ALL_TI_YMD: str
    "시간표일자"
    DGHT_CRSE_SC_NM: str
    "주야과정명"
    ORD_SC_NM: str
    "계열명"
    DDDEP_NM: str
    "학과명"
    GRADE: str
    "학년"
    CLRM_NM: str
    "강의실명"
    CLASS_NM: str
    "학급명"
    PERIO: str
    "교시"
    ITRT_CNTNT: str
    "수업내용"
    LOAD_DTM: str
    "수정일"


class HisTimeTableDict(TypedDict):
    hisTimetable: NeisDict[HisTimeTableRowDict]
