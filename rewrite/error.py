class NeispyException(Exception):
    pass

class HTTPException(NeispyException):
    pass

class MissingRequiredValues(NeispyException):
    pass

class AuthenticationKeyInvaild(NeispyException):
    pass

class ServiceNotFound(NeispyException):
    pass

class LocationValueTypeInvaild(NeispyException):
    pass

class CannotExceed1000(NeispyException):
    pass

class DailyTrafficLimit(NeispyException):
    pass

class ServerError(NeispyException):
    pass

class DatabaseConnectionError(NeispyException):
    pass

class SQLStatementError(NeispyException):
    pass

class LimitUseAuthenticationkey(NeispyException):
    pass

class DataNotFound(NeispyException):
    pass
