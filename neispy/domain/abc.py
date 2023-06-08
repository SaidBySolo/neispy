from dataclasses import dataclass
from typing import Any, Dict, Generic, List, Tuple, TypeVar


from typing_extensions import Self

from neispy.types.base import (
    DescriptionDict,
    ResultDict,
    ListTotalCountDict,
    HeadDict,
    RowDict,
)


R = TypeVar("R", bound="AbstractRow")


@dataclass
class Description:
    CODE: str
    MESSAGE: str

    @classmethod
    def from_dict(cls, d: DescriptionDict) -> "Description":
        return cls(
            CODE=d["CODE"],
            MESSAGE=d["MESSAGE"],
        )


@dataclass
class Result:
    RESULT: Description

    @classmethod
    def from_dict(cls, d: ResultDict) -> "Result":
        return cls(RESULT=Description.from_dict(d["RESULT"]))


@dataclass
class ListTotalCount:
    list_total_count: int

    @classmethod
    def from_dict(cls, d: ListTotalCountDict) -> "ListTotalCount":
        return cls(list_total_count=d["list_total_count"])


@dataclass
class Head:
    head: Tuple[ListTotalCount, Result]

    @classmethod
    def from_dict(cls, d: HeadDict) -> "Head":
        return cls(
            head=(
                ListTotalCount.from_dict(d["head"][0]),
                Result.from_dict(d["head"][1]),
            )
        )


class AbstractRow:
    @classmethod
    def from_dict(cls, d: dict[str, str]) -> Self:
        return cls(**d)


@dataclass
class Row(Generic[R]):
    row: List[R]

    @classmethod
    def from_dict(cls, d: List[R]) -> "Row[R]":
        return cls(row=d)


NeisData = Tuple[Head, Row[R]]
