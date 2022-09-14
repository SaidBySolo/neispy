from datetime import datetime, timedelta, timezone

KST = timezone(timedelta(hours=9))


def now() -> str:
    return datetime.now(tz=KST).strftime("%Y%m%d")
