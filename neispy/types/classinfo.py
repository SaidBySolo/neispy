from typing import Optional

from typing_extensions import TypedDict

from neispy.types.base import NeisDict, SchoolRelatedBaseDict


class ClassInfoRowDict(SchoolRelatedBaseDict):
    AY: str
    "학년도"
    GRADE: str
    "학년"
    DGHT_CRSE_SC_NM: Optional[str]
    "주야과정명"
    SCHUL_CRSE_SC_NM: str
    "학교과정명"
    ORD_SC_NM: Optional[str]
    "계열명"
    DDDEP_NM: Optional[str]
    "학과명"
    CLASS_NM: str
    "학급명"
    LOAD_DTM: str
    "수정일"


class ClassInfoDict(TypedDict):
    classInfo: NeisDict[ClassInfoRowDict]
