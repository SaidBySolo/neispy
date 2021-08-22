class NeispyException(Exception):
    pass


class ArgumentError(NeispyException):
    def __init__(self):
        super().__init__("인자값이 틀립니다.")


class HTTPException(NeispyException):
    def __init__(self, code: int, message: str):
        super().__init__(f"{code} {message}")


class MissingRequiredValues(HTTPException):
    pass


class AuthenticationKeyInvaild(HTTPException):
    pass


class ServiceNotFound(HTTPException):
    pass


class LocationValueTypeInvaild(HTTPException):
    pass


class CannotExceed1000(HTTPException):
    pass


class DailyTrafficLimit(HTTPException):
    pass


class ServerError(HTTPException):
    pass


class DatabaseConnectionError(HTTPException):
    pass


class SQLStatementError(HTTPException):
    pass


class LimitUseAuthenticationkey(HTTPException):
    pass


class DataNotFound(HTTPException):
    pass


ExceptionsMapping = {
    "INFO-200": DataNotFound,
    "INFO-300": LimitUseAuthenticationkey,
    "ERROR-290": AuthenticationKeyInvaild,
    "ERROR-300": MissingRequiredValues,
    "ERROR-310": ServiceNotFound,
    "ERROR-333": LocationValueTypeInvaild,
    "ERROR-336": CannotExceed1000,
    "ERROR-337": DailyTrafficLimit,
    "ERROR-500": ServerError,
    "ERROR-600": DatabaseConnectionError,
    "ERROR-601": SQLStatementError,
}
