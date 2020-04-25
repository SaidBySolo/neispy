import aiohttp
import datetime

n = datetime.datetime.now()
now = f'{n.year}{n.month}{n.day}'

apimain = "https://open.neis.go.kr/hub/mealServiceDietInfo" #오픈 api요청주소

async def lunchinfo(param, ATPT_OFCDC_SC_CODE, SD_SCHUL_CODE, MLSV_YMD=now):
    """
    ``param``은 필수인자입니다.

    ``ATPT_OFCDC_SC_CODE``은 시도교육청코드 입니다.

    ``SD_SCHUL_CODE``은 표준학교코드 입니다.

    ``MLSV_YMD``은 급식을 불러올 날짜를 지정할수있습니다.

    인자값을 주지않은경우에는 현재날짜로 급식을 불러옵니다.

    요청한 값은 ``str``로 반환됩니다.
    """
    AE = f'&ATPT_OFCDC_SC_CODE={ATPT_OFCDC_SC_CODE}'
    SE = f'&SD_SCHUL_CODE={SD_SCHUL_CODE}'
    MD = f'&MLSV_YMD={MLSV_YMD}'
    async with aiohttp.ClientSession() as cs:
        async with cs.get(apimain + param + AE + SE + MD) as r:
            response = await r.text()
            return response