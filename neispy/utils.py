from datetime import datetime, timedelta, timezone
from typing import Any, Tuple, get_type_hints

from typing_extensions import Self

from neispy.domain.abc import AbstractRow, Head, Row

KST = timezone(timedelta(hours=9))


def now() -> str:
    return datetime.now(tz=KST).strftime("%Y%m%d")


class Deserializer:
    @classmethod
    def from_dict(cls, d: Any) -> Self:
        annotations = get_type_hints(cls)
        key = list(annotations.keys())[0]
        # 유형주석의 첫번째는 튜플형식 입니다.
        # 튜플의 첫번째는 Head이고 두번째는 Row입니다.
        # 그러므로 __args__[1]을 사용하여 Row를 가져옵니다.
        # Row의 제네릭 타입을 가져와서 객체를 생성해야하기 때문에 다시 __args__[0]을 사용합니다.
        row_type: AbstractRow = list(annotations.values())[0].__args__[1].__args__[0]
        obj: Tuple[Head, Row[Any]] = (
            Head.from_dict(d[key][0]),
            Row.from_dict([row_type.from_dict(d) for d in d[key][1]["row"]]),
        )
        return cls(**{key: obj})
