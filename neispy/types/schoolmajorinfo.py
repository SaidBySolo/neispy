from typing_extensions import TypedDict

from neispy.types.base import NeisDict, SchoolRelatedBaseDict


class SchoolMajorInfoRowDict(SchoolRelatedBaseDict):
    DGHT_CRSE_SC_NM: str
    "주야과정명"
    ORD_SC_NM: str
    "계열명"
    DDDEP_NM: str
    "학과명"
    LOAD_DTM: str
    "수정일"


class SchoolMajorInfoDict(TypedDict):
    schoolMajorInfo: NeisDict[SchoolMajorInfoRowDict]
