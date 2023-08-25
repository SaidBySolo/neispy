from __future__ import annotations

from dataclasses import dataclass

from neispy.domain.abc import NeisObject, SchoolRelated
from neispy.types.elstimetable import ElsTimeTableDict
from neispy.utils import Deserializer


@dataclass
class ElsTimeTableRow(SchoolRelated):
    AY: str
    "학년도"
    SEM: str
    "학기"
    ALL_TI_YMD: str
    "시간표일자"
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
class ElsTimeTable(Deserializer):
    elsTimetable: NeisObject[ElsTimeTableRow]

    @classmethod
    def from_dict(cls, d: ElsTimeTableDict) -> ElsTimeTable:
        return super().from_dict(d)
