import aiohttp
import json

apimain = "https://open.neis.go.kr/hub/schoolInfo" 
        
async def schoolinfo(param, schoolname):
    """
    ``param``은 필수인자값입니다.

    ``schoolname``은 학교 이름을 받습니다.

    요청한값은 ``str``형식으로 반환합니다.
    """
    schul_nm = f'&SCHUL_NM={schoolname}'
    async with aiohttp.ClientSession() as cs:
        async with cs.get(apimain + param + schul_nm) as r:
            response = await r.text()
            return response


