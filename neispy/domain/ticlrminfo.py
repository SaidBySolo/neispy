from __future__ import annotations

from dataclasses import dataclass

from neispy.domain.abc import NeisObject, SchoolRelated
from neispy.types.ticlrminfo import TiClrmInfoDict
from neispy.utils import Deserializer


@dataclass
class TiClrmInfoRow(SchoolRelated):
    AY: str
    "학년도"
    GRADE: str
    "학년"
    SEM: str
    "학기"
    SCHUL_CRSE_SC_NM: str
    "학교과정명"
    DGHT_CRSE_SC_NM: str
    "주야과정명"
    ORD_SC_NM: str
    "계열명"
    DDDEP_NM: str
    "학과명"
    CLRM_NM: str
    "강의실명"
    LOAD_DTM: str
    "수정일"


@dataclass
class TiClrmInfo(Deserializer):
    tiClrminfo: NeisObject[TiClrmInfoRow]

    @classmethod
    def from_dict(cls, d: TiClrmInfoDict) -> TiClrmInfo:
        return super().from_dict(d)
