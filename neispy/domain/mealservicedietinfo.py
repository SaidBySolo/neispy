from __future__ import annotations

from dataclasses import dataclass

from neispy.domain.abc import NeisObject, AbstractRow
from neispy.types.mealservicedietinfo import MealServiceDietInfoDict
from neispy.utils import Deserializer


@dataclass
class MealServiceDietInfoRow(AbstractRow):
    ATPT_OFCDC_SC_CODE: str
    "시도교육청코드"
    ATPT_OFCDC_SC_NM: str
    "시도교육청명"
    SD_SCHUL_CODE: str
    "표준학교코드"
    SCHUL_NM: str
    "학교명"
    MMEAL_SC_CODE: str
    "식사코드"
    MMEAL_SC_NM: str
    "식사명"
    MLSV_YMD: str
    "급식일자"
    MLSV_FGR: str
    "급식인원수"
    DDISH_NM: str
    "요리명"
    ORPLC_INFO: str
    "원산지정보"
    CAL_INFO: str
    "칼로리정보"
    NTR_INFO: str
    "영양정보"
    MLSV_FROM_YMD: str
    "급식시작일자"
    MLSV_TO_YMD: str
    "급식종료일자"


@dataclass
class MealServiceDietInfo(Deserializer):
    schoolInfo: NeisObject[MealServiceDietInfoRow]

    @classmethod
    def from_dict(cls, d: MealServiceDietInfoDict) -> MealServiceDietInfo:
        return super().from_dict(d)
