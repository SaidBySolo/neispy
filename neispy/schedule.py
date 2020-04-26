import aiohttp
import datetime

n = datetime.datetime.now()
now = f'{n.year}{n.month}{n.day}'

apimain = 'https://open.neis.go.kr/hub/SchoolSchedule'

async def schoolshd(param, ATPT_OFCDC_SC_CODE=None, SD_SCHUL_CODE=None, 
DGHT_CRSE_SC_NM=None, SCHUL_CRSE_SC_NM=None, 
AA_YMD=now, AA_FROM_YMD=None, AA_TO_YMD=None):
    """
    ``param``은 필수인자입니다.

    ``ATPT_OFCDC_SC_CODE``은 시도교육청코드를 받습니다.

    ``SD_SCHUL_CODE``은 표준학교코드를 받습니다.

    ``DGHT_CRSE_SC_NM``은 주야과정명을 받습니다.

    ``SCHUL_CRSE_SC_NM``은 학교과정명을 받습니다

    ``AA_YMD``은 학사일자를 받습니다.

    ``AA_FROM_YMD``은 학사시작일자를 받습니다.

    ``AA_TO_YMD``은 학사종료일자를받습니다.

    ``AA_YMD``를 인자값을 주지않은경우에는 현재날짜로 일정을 불러옵니다.

    요청한값은 ``str``형식으로 반환합니다.
    """

    paramlist = []
    
    if ATPT_OFCDC_SC_CODE is not None:
        AOSC = f'&ATPT_OFCDC_SC_CODE={ATPT_OFCDC_SC_CODE}'
        paramlist.append(AOSC)

    if SD_SCHUL_CODE is not None:
        ASC = f'&SD_SCHUL_CODE={SD_SCHUL_CODE}'
        paramlist.append(ASC)

    if DGHT_CRSE_SC_NM is not None:
        DCSN = f'&DGHT_CRSE_SC_NM={DGHT_CRSE_SC_NM}'
        paramlist.append(DCSN)

    if SCHUL_CRSE_SC_NM is not None:
        SCSN = f'&SCHUL_CRSE_SC_NM={SCHUL_CRSE_SC_NM}'
        paramlist.append(SCSN)

    if AA_YMD is not None:
        AY = f'&AA_YMD={AA_YMD}'
        paramlist.append(AY)
    
    if AA_FROM_YMD is not None:
        AFY = f'&AA_FROM_YMD={AA_FROM_YMD}'
        paramlist.append(AFY)
    
    if AA_TO_YMD is not None:
        ATY = f'&AA_TO_YMD={AA_TO_YMD}'
        paramlist.append(ATY)

    totalparam = f'{apimain}{param}{"".join(paramlist)}'
    async with aiohttp.ClientSession() as cs:
        async with cs.get(totalparam) as r:
            response = await r.text()
            return response