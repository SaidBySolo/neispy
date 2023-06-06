from typing_extensions import NotRequired

from neispy.params.abc import AbstractSchoolRelatedRequestParams


class SchoolScheduleParams(AbstractSchoolRelatedRequestParams):
    DGHT_CRSE_SC_NM: NotRequired[str]
    SCHUL_CRSE_SC_NM: NotRequired[str]
    AA_YMD: NotRequired[int]
    AA_FROM_YMD: NotRequired[int]
    AA_TO_YMD: NotRequired[int]
