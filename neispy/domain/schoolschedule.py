from __future__ import annotations

from dataclasses import dataclass

from neispy.domain.abc import NeisObject, AbstractRow

from neispy.utils import Deserializer
from neispy.types import SchoolScheduleDict


@dataclass
class SchoolScheduleRow(AbstractRow):
    ATPT_OFCDC_SC_CODE: str
    "시도교육청코드"
    ATPT_OFCDC_SC_NM: str
    "시도교육청명"
    SD_SCHUL_CODE: str
    "표준학교코드"
    SCHUL_NM: str
    "학교명"
    AY: str
    "학년도"
    DGHT_CRSE_SC_NM: str
    "주야과정명"
    SCHUL_CRSE_SC_NM: str
    "학교과정명"
    SBTR_DD_SC_NM: str
    "수업공제일명"
    AA_YMD: str
    "학사일자"
    EVENT_NM: str
    "행사명"
    EVENT_CNTNT: str
    "행사내용"
    ONE_GRADE_EVENT_YN: str
    "1학년행사여부"
    TW_GRADE_EVENT_YN: str
    "2학년행사여부"
    THREE_GRADE_EVENT_YN: str
    "3학년행사여부"
    FR_GRADE_EVENT_YN: str
    "4학년행사여부"
    FIV_GRADE_EVENT_YN: str
    "5학년행사여부"
    SIX_GRADE_EVENT_YN: str
    "6학년행사여부"
    LOAD_DTM: str
    "수정"


@dataclass
class SchoolSchedule(Deserializer):
    SchoolSchedule: NeisObject[SchoolScheduleRow]

    @classmethod
    def from_dict(cls, d: SchoolScheduleDict) -> SchoolSchedule:
        return super().from_dict(d)
