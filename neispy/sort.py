import json

async def sort_reqarg(KEY='', Type='json', pIndex=str(1), pSize=str(100)):
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

async def sort_lunchmenu(data):
    """
    json형식만 받아옵니다.

    json을 정리하여 급식 메뉴만을 ``str``로 반환합니다.
    """
    loaddata = json.loads(data)
    datalist = loaddata['mealServiceDietInfo']
    datadict = datalist[1]
    datalist1 = datadict['row']
    datadict1 = datalist1[0]
    result = datadict1['DDISH_NM']
    linebreak = result.replace('<br/>', '\n')
    return linebreak

async def sort_schoolcode(data):
    """
    json형식만 받아옵니다.

    json을 정리하여 시도교육청코드,표준학교코드를 ``tuple``로 반환합니다.
    """
    loaddata = json.loads(data)
    datalist = loaddata['schoolInfo']
    datadict = datalist[1]
    datalist1 = datadict['row']
    datadict1 = datalist1[0]
    SC_CODE = datadict1['ATPT_OFCDC_SC_CODE']
    SD_SCHUL_CODE = datadict1['SD_SCHUL_CODE']
    return(SC_CODE, SD_SCHUL_CODE)

async def sort_scdname(data):
    loaddata = json.loads(data)
    datalist = loaddata['SchoolSchedule']
    datadict = datalist[1]
    datalist1 = datadict['row']
    datadict1 = datalist1[0]
    result = datadict1['EVENT_NM']
    return(result)

