from typing_extensions import NotRequired

from neispy.params.schoolmajorinfo import SchoolMajorInfoParams


class ClassInfoParams(SchoolMajorInfoParams):
    AY: NotRequired[str]
    GRADE: NotRequired[str]
    SCHUL_CRSE_SC_NM: NotRequired[str]
    DDDEP_NM: NotRequired[str]
