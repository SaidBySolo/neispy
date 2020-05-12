import asyncio
import aiohttp
import json


class Http:

    def __init__(self, KEY, Type, pIndex, pSize):
        self.requirement_query = self.requirement(KEY, Type, pIndex, pSize)

    async def request(self, method, url, query):

        base_url = 'https://open.neis.go.kr'
        URL = base_url + url + self.requirement_query + query

        async with aiohttp.ClientSession() as cs:
            async with cs.request(method, URL) as r:
                response = await r.text()
                data = json.loads(response)
                data['schoolInfo']

    def requirement(self, KEY, Type, pIndex, pSize):
        """
        ``KEY``는 Open APi키를 필요로합니다. 없을경우 샘플키로 요청합니다.

        ``Type``는 json 또는 xml값을 요청할수있습니다. 기본값은 json입니다.

        ``pIndex``는 페이지 위치입니다. 기본값은 1입니다.

        ``pSize``는 페이지 당 신청 숫자입니다. 기본값은 100입니다

        ``str``로 반환됩니다.
        """
        apikey = f"?KEY={KEY}"
        reqtype = f"&Type={Type}"
        pindex = f"&pindex={pIndex}"
        psize = f"&pSize={pSize}"
        return(apikey + reqtype + pindex + psize)

    async def schoolInfo(self, query):
        return await self.request('get', '/hub/schoolInfo', query)
        

    async def mealServiceDietInfo(self, query):
        return await self.request('get', '/hub/mealServiceDietInfo', query)
        

    async def SchoolSchedule(self, query):
        return await self.request('get', '/hub/SchoolSchedule', query)
        
