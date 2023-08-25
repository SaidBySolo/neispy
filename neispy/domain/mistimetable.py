from __future__ import annotations

from dataclasses import dataclass

from neispy.domain.abc import NeisObject, SchoolRelated
from neispy.types.mistimetable import MisTimeTableDict
from neispy.utils import Deserializer


@dataclass
class MisTimeTableRow(SchoolRelated):
    AY: str
    "학년도"
    SEM: str
    "학기"
    ALL_TI_YMD: str
    "시간표일자"
    DGHT_CRSE_SC_NM: str
    "주야과정명"
    GRADE: str
    "학년"
    CLASS_NM: str
    "학급명"
    PERIO: str
    "교시"
    ITRT_CNTNT: str
    "수업내용"
    LOAD_DTM: str
    "수정일"


@dataclass
class MisTimeTable(Deserializer):
    misTimetable: NeisObject[MisTimeTableRow]

    @classmethod
    def from_dict(cls, d: MisTimeTableDict) -> MisTimeTable:
        return super().from_dict(d)
