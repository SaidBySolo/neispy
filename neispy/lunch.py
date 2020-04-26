import aiohttp
import datetime

n = datetime.datetime.now()
now = f'{n.year}{n.month}{n.day}'

apimain = "https://open.neis.go.kr/hub/mealServiceDietInfo" #오픈 api요청주소

async def lunchinfo(param, ATPT_OFCDC_SC_CODE=None, SD_SCHUL_CODE=None,
MMEAL_SC_CODE=None, MLSV_YMD=now, MLSV_FROM_YMD=None, MLSV_TO_YMD=None) :
    """
    ``param``은 필수인자입니다.

    ``ATPT_OFCDC_SC_CODE``은 시도교육청코드를 받습니다.

    ``SD_SCHUL_CODE``은 표준학교코드를 받습니다.

    ``MMEAL_SC_CODE``은 식사코드를 받습니다.

    ``MLSV_YMD``은 급식일자를 받습니다.

    ``MLSV_FROM_YMD``은 급식시작일자를 받습니다.

    ``MLSV_TO_YMD``은 급식종료일자를 받습니다.

    ``MLSV_TO_YMD`` 인자값을 주지않은경우에는 현재날짜로 급식을 불러옵니다.

    요청한 값은 ``str``로 반환됩니다.
    """
    
    paramlist = []

    if ATPT_OFCDC_SC_CODE is not None:
        AOSC = f'&ATPT_OFCDC_SC_CODE={ATPT_OFCDC_SC_CODE}'
        paramlist.append(AOSC)

    if SD_SCHUL_CODE is not None:
        ASC = f'&SD_SCHUL_CODE={SD_SCHUL_CODE}'
        paramlist.append(ASC)

    if MLSV_YMD is not None:
        MY = f'&MLSV_YMD={MLSV_YMD}'
        paramlist.append(MY)

    if MLSV_FROM_YMD is not None:
        MFY = f'&MLSV_FROM_YMD={MLSV_FROM_YMD}'
        paramlist.append(MFY)

    if MLSV_TO_YMD is not None:
        MTY = f'&MLSV_TO_YMD={MLSV_TO_YMD}'
        paramlist.append(MTY)
    
    totalparam = f'{apimain}{param}{"".join(paramlist)}'
    async with aiohttp.ClientSession() as cs:
        async with cs.get(totalparam) as r:
            response = await r.text()
            return response