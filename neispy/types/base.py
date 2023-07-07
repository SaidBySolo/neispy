from typing import Generic, Tuple, TypeVar

T = TypeVar("T")

from typing_extensions import TypedDict


class DescriptionDict(TypedDict):
    CODE: str
    MESSAGE: str


class ResultDict(TypedDict):
    RESULT: DescriptionDict


class ListTotalCountDict(TypedDict):
    list_total_count: int


class HeadDict(TypedDict):
    head: Tuple[ListTotalCountDict, ResultDict]


class RowDict(TypedDict, Generic[T]):
    row: list[T]


NeisDict = Tuple[HeadDict, RowDict[T]]
