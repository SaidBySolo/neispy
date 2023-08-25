from typing_extensions import NotRequired

from neispy.params.abc import AbstractSchoolRelatedRequestParams


class MealServiceDietInfoParams(AbstractSchoolRelatedRequestParams):
    MMEAL_SC_CODE: NotRequired[str]
    MLSV_YMD: NotRequired[str]
    MLSV_FROM_YMD: NotRequired[str]
    MLSV_TO_YMD: NotRequired[str]
