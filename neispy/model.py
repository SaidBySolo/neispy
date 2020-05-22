from .error import ArgumentError


class NeispyResponse:
    def __init__(self, response, sort, rawlist=False):
        """모든 모델의 기본이되는 클래스입니다.

        Arguments:

            `response` {str} -- json형식의 값을 넣어주셔야합니다.

            `sort` {str} -- 밑의 항목에 있는 정리하고자하는 정보를 넣어주셔야하는 곳입니다.

        Keyword Arguments:

            `rawlist` {bool} -- 여러개의 리스트를 받아올것인지에 대한 여부입니다. (default: {False})

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
                     'classInfo',
                     'elsTimetable',
                     'misTimetable',
                     'hisTimetable']
        if sort in sort_list:
            if sort == sort_list[3] or sort == sort_list[4] or sort == sort_list[5]:
                datalist = response[sort]
                datadict = datalist[1]['row']
                self.data = datadict
            elif rawlist is True:
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


class NeispySchoolInfo(NeispyResponse):
    def __init__(self, response, sort='schoolInfo', rawlist=False):
        super().__init__(response, sort=sort, rawlist=rawlist)


class NeispySchoolSchedule(NeispyResponse):
    def __init__(self, response, sort='SchoolSchedule', rawlist=False):
        super().__init__(response, sort=sort, rawlist=rawlist)


class NeispyMealServiceDietInfo(NeispyResponse):
    def __init__(self, response, sort='mealServiceDietInfo', rawlist=False):
        super().__init__(response, sort=sort, rawlist=rawlist)

    def meal(self):
        """
        급식 메뉴만을 줄바꿈하여 ``str``로 반환합니다.
        """
        result = self.data['DDISH_NM']
        linebreak = result.replace('<br/>', '\n')
        return linebreak


class NeispyTimeTable(NeispyResponse):
    def __init__(self, response, sort):
        super().__init__(response, sort)

    def timetable(self):
        """
        첫번째 교시부터 순서대로 ``list``로 반환합니다.
        """
        result = [f['ITRT_CNTNT'] for f in self.data]
        return result

class NeisptClassInfo(NeispyResponse):
    def __init__(self, response, sort='classInfo', rawlist=False):
        super().__init__(response, sort, rawlist=rawlist)
