from typing_extensions import NotRequired

from neispy.params.abc import AbstractSchoolRelatedRequestParams


class SchoolInfoParams(AbstractSchoolRelatedRequestParams):
    SCHUL_NM: NotRequired[str]
    SCHUL_KND_SC_NM: NotRequired[str]
    LCTN_SC_NM: NotRequired[str]
    FOND_SC_NM: NotRequired[str]
