class NeispyException(Exception):
    pass


class APIKeyNotFound(NeispyException):
    def __init__(self):
        super().__init__("API키를 찾을수없습니다. 샘플키로 요청합니다.")


class ArgumentError(NeispyException):
    def __init__(self):
        super().__init__("인자값이 틀립니다.")


class HTTPException(NeispyException):
    def __init__(self, code, message):
        super().__init__(f'{code} {message}')


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
