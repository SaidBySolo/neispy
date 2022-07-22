from datetime import timezone, datetime, timedelta


KST = timezone(timedelta(hours=9))


def now() -> str:
    return datetime.now(tz=KST).strftime("%Y%m%d")
