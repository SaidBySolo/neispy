import aiohttp
import ujson
from .check import status_info, check_apikey
from .error import (
    APIKeyNotFound,
    MissingRequiredValues,
    AuthenticationKeyInvaild,
    ServiceNotFound,
    LocationValueTypeInvaild,
    CannotExceed1000,
    DailyTrafficLimit,
    ServerError,
    DatabaseConnectionError,
    SQLStatementError,
    LimitUseAuthenticationkey,
    DataNotFound,
    HTTPException,
)


class AsyncHttp:
    def __init__(self, KEY, Type, pIndex, pSize, force):
        try:
            check_apikey(key)
        except APIKeyNotFound:
            if force is True:
                pass
            else:
                raise APIKeyNotFound

        self.requirement_query = self.requirement(KEY, Type, pIndex, pSize)

    async def request(self, method, url, query) -> dict:
        base_url = "https://open.neis.go.kr/hub/"
        URL = base_url + url + self.requirement_query + query

        async with aiohttp.ClientSession() as cs:
            async with cs.request(method, URL) as r:
                response = await r.text()
                try:
                    data = ujson.loads(response)
                except Exception:
                    raise HTTPException(
                        r.status, "API서버로부터 잘못된 응답을 받았습니다. 서버 상태를 확인해주세요"
                    )
                code, msg = status_info(data, url)

                if code == "INFO-000":
                    return data

                if code == "ERROR-300":
                    raise MissingRequiredValues(code, msg)
                elif code == "ERROR-290":
                    raise AuthenticationKeyInvaild(code, msg)
                elif code == "ERROR-310":
                    raise ServiceNotFound(code, msg)
                elif code == "ERROR-333":
                    raise LocationValueTypeInvaild(code, msg)
                elif code == "ERROR-336":
                    raise CannotExceed1000(code, msg)
                elif code == "ERROR-337":
                    raise DailyTrafficLimit(code, msg)
                elif code == "ERROR-500":
                    raise ServerError(code, msg)
                elif code == "ERROR-600":
                    raise DatabaseConnectionError(code, msg)
                elif code == "ERROR-601":
                    raise SQLStatementError(code, msg)
                elif code == "INFO-300":
                    raise LimitUseAuthenticationkey(code, msg)
                elif code == "INFO-200":
                    raise DataNotFound(code, msg)
                else:
                    raise HTTPException(code, msg)

    @classmethod
    def requirement(cls, KEY, Type, pIndex, pSize) -> tuple:
        apikey = f"?KEY={KEY}"
        reqtype = f"&Type={Type}"
        pindex = f"&pindex={pIndex}"
        psize = f"&pSize={pSize}"
        return apikey + reqtype + pindex + psize

    async def schoolInfo(self, query) -> dict:
        return await self.request("get", "schoolInfo", query)

    async def mealServiceDietInfo(self, query) -> dict:
        return await self.request("get", "mealServiceDietInfo", query)

    async def SchoolSchedule(self, query) -> dict:
        return await self.request("get", "SchoolSchedule", query)

    async def acaInsTiInfo(self, query) -> dict:
        return await self.request("get", "acaInsTiInfo", query)

    async def timeTable(self, schclass, query) -> dict:
        return await self.request("get", f"{schclass}Timetable", query)

    async def classInfo(self, query) -> dict:
        return await self.request("get", "classInfo", query)

    async def schoolMajorinfo(self, query) -> dict:
        return await self.request("get", "schoolMajorinfo", query)

    async def schulAflcoinfo(self, query) -> dict:
        return await self.request("get", "schulAflcoinfo", query)

    async def tiClrminfo(self, query) -> dict:
        return await self.request("get", "tiClrminfo", query)

    async def spsTimetable(self, query) -> dict:
        return await self.request("get", "spsTimetable", query)
