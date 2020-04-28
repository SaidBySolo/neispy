import aiohttp
import datetime

apimain = 'https://open.neis.go.kr/hub/elsTimetable'#요청주소

n = datetime.datetime.now()
now = f'{n.year}{n.month}{n.day}'

async def timetable(param,ATPT_OFCDC_SC_CODE=None,
SD_SCHUL_CODE=None,AY=None,SEM=None,ALL_TI_YMD=None,
GRADE=None,CLASS_NM=None,PERIO=None,TI_FROM_YMD=None,TI_TO_YMD=None):
    """
    ``param``은 필수인자입니다.

    ``ATPT_OFCDC_SC_CODE``은 시도교육청코드를 받습니다.(필수)

    ``SD_SCHUL_CODE``은 표준학교코드를 받습니다.(필수)

    ``AY``은 학년도를 받습니다.

    ``SEM``은 학기를 받습니다.

    ``ALL_TI_YMD``은 시간표일자를 받습니다.

    ``GRADE``은 학년을 받습니다.

    ``CLASS_NM``은 반명을 받습니다.

    ``PERIO``은 교시를 받습니다.

    ``TI_FROM_YMD``은 시간표시작일자를 받습니다.

    ``TI_TO_YMD``은 시간표종료일자를 받습니다.
    """

    paramlist = []

    if ATPT_OFCDC_SC_CODE is not None:
        AOSC = f'&ATPT_OFCDC_SC_CODE={ATPT_OFCDC_SC_CODE}'
        paramlist.append(AOSC)

    if SD_SCHUL_CODE is not None:
        ASC = f'&SD_SCHUL_CODE={SD_SCHUL_CODE}'
        paramlist.append(ASC)

    if AY is not None:
        AY = f'&AY={AY}'
        paramlist.append(AY)

    if SEM is not None:
        SEM = f'&SEM={SEM}'
        paramlist.append(SEM)

    if ALL_TI_YMD is not None:
        ATY = f'&ALL_TI_YMD={ALL_TI_YMD}'
        paramlist.append(ATY)

    if GRADE is not None:
        GE = f'&GRADE={GRADE}'
        paramlist.append(GE)

    if CLASS_NM is not None:
        CN = f'&CLASS_NM={CLASS_NM}'
        paramlist.append(CN)

    if PERIO is not None:
        PO = f'&PERIO={PERIO}'
        paramlist.append(PO)

    if TI_FROM_YMD is not None:
        TFY = f'&TI_FROM_YMD={TI_FROM_YMD}'
        paramlist.append(TFY)

    if TI_TO_YMD is not None:
        TTY = f'&TI_TO_YMD={TI_TO_YMD}'
        paramlist.append(TTY)

    totalparam = f'{apimain}{param}{"".join(paramlist)}'
    async with aiohttp.ClientSession() as cs:
        async with cs.get(totalparam) as r:
            response = await r.text()
            return response