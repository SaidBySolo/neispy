from typing_extensions import NotRequired

from neispy.params.abc import AbstractRequestParams


class AcaInsTiInfoParams(AbstractRequestParams):
    ADMST_ZONE_NM: NotRequired[str]
    ACA_ASNUM: NotRequired[str]
    REALM_SC_NM: NotRequired[str]
    LE_ORD_NM: NotRequired[str]
    LE_CRSE_NM: NotRequired[str]
