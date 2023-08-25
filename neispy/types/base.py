from typing import Generic, List, Tuple, TypeVar

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
    row: List[T]


class BaseDict(TypedDict):
    ATPT_OFCDC_SC_CODE: str
    "시도교육청코드"
    ATPT_OFCDC_SC_NM: str
    "시도교육청명"


class SchoolRelatedBaseDict(BaseDict):
    SD_SCHUL_CODE: str
    "표준학교코드"
    SCHUL_NM: str
    "학교명"


NeisDict = Tuple[HeadDict, RowDict[T]]
