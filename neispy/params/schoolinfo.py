from typing_extensions import NotRequired

from neispy.params.abc import AbstractNotRequiredSchoolRelatedRequestParams


class SchoolInfoParams(AbstractNotRequiredSchoolRelatedRequestParams):
    SCHUL_NM: NotRequired[str]
    SCHUL_KND_SC_NM: NotRequired[str]
    LCTN_SC_NM: NotRequired[str]
    FOND_SC_NM: NotRequired[str]
