import aiohttp
from .http import Http

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
    
        response = await self.http.schoolInfo(query)
        return response
        


    async def mealServiceDietInfo(self):
        pass

    async def SchoolSchedule(self):
        pass