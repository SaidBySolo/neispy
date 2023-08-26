from __future__ import annotations

from dataclasses import dataclass

from neispy.domain.abc import NeisObject, SchoolRelated
from neispy.types.schulaflcoinfo import SchulAflcoInfoDict
from neispy.utils import Deserializer


@dataclass
class SchulAflcoInfoRow(SchoolRelated):
    DGHT_CRSE_SC_NM: str
    "주야과정명"
    ORD_SC_NM: str
    "계열명"
    LOAD_DTM: str
    "수정일"


@dataclass
class SchulAflcoInfo(Deserializer):
    schulAflcoinfo: NeisObject[SchulAflcoInfoRow]

    @classmethod
    def from_dict(cls, d: SchulAflcoInfoDict) -> SchulAflcoInfo:
        return super().from_dict(d)
