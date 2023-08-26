from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, List, Tuple, TypeVar

from typing_extensions import Self

from neispy.types.base import DescriptionDict, HeadDict, ListTotalCountDict, ResultDict

R = TypeVar("R", bound="AbstractRow")


@dataclass
class Description:
    CODE: str
    MESSAGE: str

    @classmethod
    def from_dict(cls, d: DescriptionDict) -> Description:
        return cls(
            CODE=d["CODE"],
            MESSAGE=d["MESSAGE"],
        )


@dataclass
class Result:
    RESULT: Description

    @classmethod
    def from_dict(cls, d: ResultDict) -> Result:
        return cls(RESULT=Description.from_dict(d["RESULT"]))


@dataclass
class ListTotalCount:
    list_total_count: int

    @classmethod
    def from_dict(cls, d: ListTotalCountDict) -> ListTotalCount:
        return cls(list_total_count=d["list_total_count"])


@dataclass
class Head:
    head: Tuple[ListTotalCount, Result]

    @classmethod
    def from_dict(cls, d: HeadDict) -> Head:
        return cls(
            head=(
                ListTotalCount.from_dict(d["head"][0]),
                Result.from_dict(d["head"][1]),
            )
        )


@dataclass
class Row(Generic[R]):
    row: List[R]

    @classmethod
    def from_dict(cls, d: List[R]) -> Row[R]:
        return cls(row=d)


@dataclass
class AbstractRow:
    ATPT_OFCDC_SC_CODE: str
    "시도교육청코드"
    ATPT_OFCDC_SC_NM: str
    "시도교육청명"

    @classmethod
    def from_dict(cls, d: dict[str, str]) -> Self:
        return cls(**d)


@dataclass
class SchoolRelated(AbstractRow):
    SD_SCHUL_CODE: str
    "표준학교코드"
    SCHUL_NM: str
    "학교명"


NeisObject = Tuple[Head, Row[R]]
