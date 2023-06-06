from typing_extensions import NotRequired

from neispy.params.abc import AbstractSchoolRelatedRequestParams


class TiClrmInfoParams(AbstractSchoolRelatedRequestParams):
    AY: NotRequired[str]
    GRADE: NotRequired[str]
    SEM: NotRequired[str]
    SCHUL_CRSE_SC_NM: NotRequired[str]
    DGHT_CRSE_SC_NM: NotRequired[str]
    ORD_SC_NM: NotRequired[str]
    DDDEP_NM: NotRequired[str]
