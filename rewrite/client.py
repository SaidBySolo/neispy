import aiohttp
import datetime
from .http import Http

n = datetime.datetime.now()
now = f'{n.year}{n.month}{n.day}'

class Client:

    def __init__(self, KEY='', Type='json', pIndex=str(1), pSize=str(100)):
        self.http = Http(KEY, Type, pIndex, pSize)
       
    async def schoolInfo(self, SD_SCHUL_CODE=None, SCHUL_NM=None, 
    SCHUL_KND_SC_NM=None, LCTN_SC_NM=None, FOND_SC_NM=None):

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

        query = "".join(paramlist)#IDK 
    
        return await self.http.schoolInfo(query)

    async def mealServiceDietInfo(self,ATPT_OFCDC_SC_CODE=None, SD_SCHUL_CODE=None,
    MMEAL_SC_CODE=None, MLSV_YMD=now, MLSV_FROM_YMD=None, MLSV_TO_YMD=None):
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
        
        query = "".join(paramlist)

        return await self.http.schoolInfo(query)
        
    async def SchoolSchedule(self, ATPT_OFCDC_SC_CODE=None, SD_SCHUL_CODE=None, DGHT_CRSE_SC_NM=None,
    SCHUL_CRSE_SC_NM=None, AA_YMD=now, AA_FROM_YMD=None, AA_TO_YMD=None):
    
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
        
        query = "".join(paramlist)

        return await self.http.schoolInfo(query)