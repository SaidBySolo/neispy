import aiohttp
import json
from .error import *


def status_info(response, querytype):
    try:
        datalist = response[querytype]
        headlist = datalist[0]['head']
        code = headlist[1]['RESULT']['CODE']
        message = headlist[1]['RESULT']['MESSAGE']
        return(code, message)
    except KeyError:
        code = response['RESULT']['CODE']
        message = response['RESULT']['MESSAGE']
        return(code, message)


def check_apikey(key):
    if any(key):
        pass
    else:
        raise APIKeyNotFound()


class AsyncHttp:

    def __init__(self, KEY, Type, pIndex, pSize):
        try:
            check_apikey(KEY)
        except APIKeyNotFound:
            import traceback
            traceback.print_exc()
        self.requirement_query = self.requirement(KEY, Type, pIndex, pSize)

    async def request(self, method, url, query):
        base_url = 'https://open.neis.go.kr/hub/'
        URL = base_url + url + self.requirement_query + query

        async with aiohttp.ClientSession() as cs:
            async with cs.request(method, URL) as r:
                response = await r.text()
                data = json.loads(response)
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
    def requirement(cls, KEY, Type, pIndex, pSize):
        apikey = f"?KEY={KEY}"
        reqtype = f"&Type={Type}"
        pindex = f"&pindex={pIndex}"
        psize = f"&pSize={pSize}"
        return(apikey + reqtype + pindex + psize)

    async def schoolInfo(self, query):
        return await self.request('get', 'schoolInfo', query)

    async def mealServiceDietInfo(self, query):
        return await self.request('get', 'mealServiceDietInfo', query)

    async def SchoolSchedule(self, query):
        return await self.request('get', 'SchoolSchedule', query)

    async def acaInsTiInfo(self, query):
        return await self.request('get', 'acaInsTiInfo', query)

    async def timeTable(self, schclass, query):
        return await self.request('get', f'{schclass}Timetable', query)

    async def classInfo(self, query):  # 이 밑까지 래핑하면 끝남
        return await self.request('get', 'classInfo', query)

    async def schoolMajorinfo(self, query):
        return await self.request('get', 'schoolMajorinfo', query)

    async def schulAflcoinfo(self, query):
        return await self.request('get', 'schulAflcoinfo', query)

    async def tiClrminfo(self, query):
        return await self.request('get', 'tiClrminfo', query)

    async def spsTimetable(self, query):
        return await self.request('get', 'spsTimetable', query)
