import aiohttp

apimain = "https://open.neis.go.kr/hub/schoolInfo" 
        
async def schoolinfo(param, SD_SCHUL_CODE=None, SCHUL_NM=None, 
SCHUL_KND_SC_NM=None, LCTN_SC_NM=None, FOND_SC_NM=None):
    """
    ``param``은 필수인자값입니다.

    ``SD_SCHUL_CODE``은 표준학교코드를 받습니다.

    ``SCHUL_NM``은 학교명을 받습니다.

    ``SCHUL_KND_SC_NM``은 학교종류명을 받습니다.

    ``LCTN_SC_NM``은 소재지명을 받습니다.

    ``FOND_SC_NM``은 설립명을받습니다

    요청한값은 ``str``형식으로 반환합니다.
    """
    
    paramlist = []

    if SD_SCHUL_CODE is not None:
        SSC = f'&SD_SCHUL_CODE={SD_SCHUL_CODE}'
        paramlist.append(SSC)

    if SCHUL_NM is not None:
        SN = f'&SCHUL_NM={SCHUL_NM}'
        paramlist.append(SN)

    if SCHUL_KND_SC_NM is not None:
        SKSN = f'&SCHUL_KND_SC_NM={SCHUL_KND_SC_NM}'
        paramlist.append(SKSN)

    if LCTN_SC_NM is not None:
        LSN = f'&LCTN_SC_NM={LCTN_SC_NM}'
        paramlist.append(LSN)

    if FOND_SC_NM is not None:
        FSN = f'&FOND_SC_NM={FOND_SC_NM}'
        paramlist.append(FSN)

    totalparam = f'{apimain}{param}{"".join(paramlist)}'
    async with aiohttp.ClientSession() as cs:
        async with cs.get(totalparam) as r:
            response = await r.text()
            return response
            
