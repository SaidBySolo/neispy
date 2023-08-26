from typing_extensions import TypedDict, NotRequired


class AbstractRequestParams(TypedDict):
    ATPT_OFCDC_SC_CODE: str


class AbstractSchoolRelatedRequestParams(AbstractRequestParams):
    SD_SCHUL_CODE: str


class AbstractNotRequiredRequestParams(TypedDict):
    ATPT_OFCDC_SC_CODE: NotRequired[str]


class AbstractNotRequiredSchoolRelatedRequestParams(AbstractNotRequiredRequestParams):
    SD_SCHUL_CODE: NotRequired[str]
