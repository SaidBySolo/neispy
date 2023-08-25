from __future__ import annotations

from dataclasses import dataclass

from neispy.domain.abc import NeisObject, SchoolRelated
from neispy.types.spstimetable import SpsTimeTableDict
from neispy.utils import Deserializer


@dataclass
class SpsTimeTableRow(SchoolRelated):
    AY: str
    "학년도"
    SEM: str
    "학기"
    ALL_TI_YMD: str
    "시간표일자"
    SCHUL_CRSE_SC_NM: str
    "학교과정명"
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
class SpsTimeTable(Deserializer):
    spsTimetable: NeisObject[SpsTimeTableRow]

    @classmethod
    def from_dict(cls, d: SpsTimeTableDict) -> SpsTimeTable:
        return super().from_dict(d)
