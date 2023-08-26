from __future__ import annotations

from dataclasses import dataclass

from neispy.domain.abc import NeisObject, SchoolRelated
from neispy.types.schoolmajorinfo import SchoolMajorInfoDict
from neispy.utils import Deserializer


@dataclass
class SchoolMajorInfoRow(SchoolRelated):
    DGHT_CRSE_SC_NM: str
    "주야과정명"
    ORD_SC_NM: str
    "계열명"
    DDDEP_NM: str
    "학과명"
    LOAD_DTM: str
    "수정일"


@dataclass
class SchoolMajorInfo(Deserializer):
    schoolMajorinfo: NeisObject[SchoolMajorInfoRow]

    @classmethod
    def from_dict(cls, d: SchoolMajorInfoDict) -> SchoolMajorInfo:
        return super().from_dict(d)
