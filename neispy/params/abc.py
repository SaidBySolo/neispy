from typing_extensions import NotRequired, TypedDict


class AbstractRequestParams(TypedDict):
    ATPT_OFCDC_SC_CODE: str
    "시도교육청코드"


class AbstractSchoolRelatedRequestParams(AbstractRequestParams):
    SD_SCHUL_CODE: str
    "표준학교코드"


class AbstractNotRequiredRequestParams(TypedDict):
    ATPT_OFCDC_SC_CODE: NotRequired[str]


class AbstractNotRequiredSchoolRelatedRequestParams(AbstractNotRequiredRequestParams):
    SD_SCHUL_CODE: NotRequired[str]
