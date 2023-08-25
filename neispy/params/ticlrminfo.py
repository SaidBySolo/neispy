from typing_extensions import NotRequired

from neispy.params.classinfo import ClassInfoParams


class TiClrmInfoParams(ClassInfoParams):
    SEM: NotRequired[str]
