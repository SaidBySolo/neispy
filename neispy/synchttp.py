import requests
import json
from .error import APIKeyNotFound, MissingRequiredValues, AuthenticationKeyInvaild, \
    ServiceNotFound, LocationValueTypeInvaild, CannotExceed1000, DailyTrafficLimit, ServerError, \
    DatabaseConnectionError, SQLStatementError, LimitUseAuthenticationkey, DataNotFound, HTTPException


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


class SyncHttp():
    def __init__(self, KEY, Type, pIndex, pSize):
        try:
            check_apikey(KEY)
        except APIKeyNotFound:
            import traceback
            traceback.print_exc()
        self.requirement_query = self.requirement(KEY, Type, pIndex, pSize)

    def request(self, url, query):
        base_url = 'https://open.neis.go.kr/hub/'
        URL = base_url + url + self.requirement_query + query
        r = requests.get(URL)
        response = r.text()
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

    def schoolInfo(self, query):
        return self.request('schoolInfo', query)

    def mealServiceDietInfo(self, query):
        return self.request('mealServiceDietInfo', query)

    def SchoolSchedule(self, query):
        return self.request('SchoolSchedule', query)

    def acaInsTiInfo(self, query):
        return self.request('acaInsTiInfo', query)

    def timeTable(self, schclass, query):
        return self.request(f'{schclass}Timetable', query)

    def classInfo(self, query):  # 이 밑까지 래핑하면 끝남
        return self.request('classInfo', query)

    def schoolMajorinfo(self, query):
        return self.request('schoolMajorinfo', query)

    def schulAflcoinfo(self, query):
        return self.request('schulAflcoinfo', query)

    def tiClrminfo(self, query):
        return self.request('tiClrminfo', query)

    def spsTimetable(self, query):
        return self.request('spsTimetable', query)
