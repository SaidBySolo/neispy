from typing_extensions import NotRequired

from neispy.params.abc import AbstractSchoolRelatedRequestParams


class ClassInfoParams(AbstractSchoolRelatedRequestParams):
    DGHT_CRSE_SC_NM: NotRequired[str]
    ORD_SC_NM: NotRequired[str]
