from __future__ import annotations

from dataclasses import dataclass

from neispy.domain.abc import NeisObject, SchoolRelated
from neispy.types.classinfo import ClassInfoDict
from neispy.utils import Deserializer


@dataclass
class ClassInfoRow(SchoolRelated):
    AY: str
    "학년도"
    GRADE: str
    "학년"
    CLASS_NM: str
    "학급명"
    DDDEP_NM: str
    "학과명"
    SCHUL_CRSE_SC_NM: str
    "학교과정명"


@dataclass
class ClassInfo(Deserializer):
    classInfo: NeisObject[ClassInfoRow]

    @classmethod
    def from_dict(cls, d: ClassInfoDict) -> ClassInfo:
        return super().from_dict(d)
