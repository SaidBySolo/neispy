class Model:
    def __init__(self, data):
        self.meal = self.sort_lunchmenu(data)
        self.code = self.sort_code(data)
        self.schdule = self.sort_schedule(data)
        self.elstimetable = self.sort_elstimetable(data)

    @classmethod
    def sort_meal(cls, data):
        """
        json형식만 받아옵니다.

        json을 정리하여 급식 메뉴만을 ``str``로 반환합니다.
        """
        datalist = data['mealServiceDietInfo']
        datadict = datalist[1]['row']
        result = datadict[0]['DDISH_NM']
        linebreak = result.replace('<br/>', '\n')
        return linebreak

    @classmethod
    def sort_code(cls, data):
        """
        json형식만 받아옵니다.

        json을 정리하여 시도교육청코드,표준학교코드를 ``tuple``로 반환합니다.
        """
        datalist = data['schoolInfo']
        datalist1 = datalist[1]['row']
        SC_CODE = datalist1[0]['ATPT_OFCDC_SC_CODE']
        SD_SCHUL_CODE = datalist1[0]['SD_SCHUL_CODE']
        return(SC_CODE, SD_SCHUL_CODE)

    @classmethod
    def sort_schedule(cls, data):
        """
        json 형식만 받아옵니다.

        json을 정리하여 학사일정명을 ``str``로 반환합니다.
        """
        datalist = data['SchoolSchedule']
        datadict = datalist[1]['row']
        result = datadict[0]['EVENT_NM']
        return result

    @classmethod
    def sort_elstimetable(cls, data):
        """
        json형식만 받아옵니다.

        json을 정리하여 첫번째 교시부터 순서대로 ``list``로 반환합니다.
        """
        datalist = data['elsTimetable']
        datalist1 = datalist[1]['row']
        result = [f['ITRT_CNTNT'] for f in datalist1]
        return result
