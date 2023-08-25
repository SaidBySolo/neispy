from typing_extensions import TypedDict


class AbstractRequestParams(TypedDict):
    ATPT_OFCDC_SC_CODE: str


class AbstractSchoolRelatedRequestParams(AbstractRequestParams):
    SD_SCHUL_CODE: str
