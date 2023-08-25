from typing_extensions import TypedDict

from neispy.types.base import NeisDict, SchoolRelatedBaseDict


class MealServiceDietInfoRowDict(SchoolRelatedBaseDict):
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


class MealServiceDietInfoDict(TypedDict):
    schoolInfo: NeisDict[MealServiceDietInfoRowDict]
