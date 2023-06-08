from typing_extensions import NotRequired

from neispy.params.ticlrminfo import TiClrmInfoParams


class TimetableParams(TiClrmInfoParams):
    ALL_TI_YMD: NotRequired[int]
    CLRM_NM: NotRequired[str]
    CLASS_NM: NotRequired[str]
    PERIO: NotRequired[int]
    TI_FROM_YMD: NotRequired[int]
    TI_TO_YMD: NotRequired[int]
