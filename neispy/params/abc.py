from typing_extensions import NotRequired, TypedDict


class AbstractRequestParams(TypedDict):
    ATPT_OFCDC_SC_CODE: NotRequired[str]


class AbstractSchoolRelatedRequestParams(AbstractRequestParams):
    SD_SCHUL_CODE: NotRequired[str]
