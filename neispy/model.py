from .error import ArgumentError


class NeispyResponse:
    def __init__(self, response, sort, rawdata: bool):
        """모든 모델의 기본이되는 클래스입니다.

        Arguments:

            `response` {str} -- json형식의 값을 넣어주셔야합니다.

            `sort` {str} -- 밑의 항목에 있는 정리하고자하는 정보를 넣어주셔야하는 곳입니다.

        Keyword Arguments:

            `rawdata` {bool} -- 여러개의 리스트를 받아올것인지에 대한 여부입니다. (default: {False})

        Lists:

            `schoolInfo` -- 학교정보입니다.

            `SchoolSchedule` -- 학사일정입니다.

            `mealServiceDietInfo` -- 급식및식단표입니다.

            `elsTimetable` -- 초등학교 시간표입니다.

            `misTimetable` -- 중학교 시간표입니다.

            `hisTimetable` -- 고등학교 시간표입니다.

        Raises:

            ArgumentError: sort에 Lists에있지않은 값을 넣을경우 Raise합니다.

        """
        sort_list = ['schoolInfo',
                     'SchoolSchedule',
                     'mealServiceDietInfo',
                     'acaInsTiInfo',
                     'classInfo',
                     'elsTimetable',
                     'misTimetable',
                     'hisTimetable']
        if sort in sort_list:
            if sort == sort_list[5] or sort == sort_list[6] or sort == sort_list[7] or rawdata is True:
                datalist = response[sort]
                datadict = datalist[1]['row']
                self.data = datadict
            else:
                datalist = response[sort]
                datadict = datalist[1]['row']
                self.data = datadict[0]
        else:
            raise ArgumentError

    def __getattr__(self, attr):
        return self.data.get(attr)

    def __dict__(self):
        return self.data


class SchoolInfo(NeispyResponse):
    def __init__(self, response, sort, rawdata):
        super().__init__(response, sort, rawdata)


class SchoolSchedule(NeispyResponse):
    def __init__(self, response, sort, rawdata):
        super().__init__(response, sort, rawdata)


class MealServiceDietInfo(NeispyResponse):
    def __init__(self, response, sort, rawdata):
        super().__init__(response, sort, rawdata)


class TimeTable(NeispyResponse):
    def __init__(self, response, sort, rawdata):
        super().__init__(response, sort, rawdata)


class ClassInfo(NeispyResponse):
    def __init__(self, response, sort, rawdata):
        super().__init__(response, sort, rawdata)


class AcaInsTiInfo(NeispyResponse):
    def __init__(self, response, sort, rawdata):
        super().__init__(response, sort, rawdata)


class ClassInfo(NeispyResponse):
    def __init__(self, response, sort, rawdata):
        super().__init__(response, sort, rawdata)