from __future__ import annotations

from dataclasses import dataclass

from neispy.domain.abc import NeisObject, SchoolRelated
from neispy.types.histimetable import HisTimeTableDict
from neispy.utils import Deserializer


@dataclass
class HisTimeTableRow(SchoolRelated):
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


@dataclass
class HisTimeTable(Deserializer):
    hisTimetable: NeisObject[HisTimeTableRow]

    @classmethod
    def from_dict(cls, d: HisTimeTableDict) -> HisTimeTable:
        return super().from_dict(d)
