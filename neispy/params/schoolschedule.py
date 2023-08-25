from typing_extensions import NotRequired

from neispy.params.schoolmajorinfo import SchoolMajorInfoParams


class SchoolScheduleParams(SchoolMajorInfoParams):
    AA_YMD: NotRequired[int]
    AA_FROM_YMD: NotRequired[int]
    AA_TO_YMD: NotRequired[int]
