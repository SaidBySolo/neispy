import neispy
import pytest

fail_list = []


@pytest.mark.asyncio
async def test_requests():
    AE = "B10"
    SE1 = "test001"
    SE2 = "test002"
    SE3 = "test003"
    itsok = "DataNotFound"
    neis = neispy.AsyncClient(force=True)

    try:
        await neis.schoolInfo()
    except Exception as e:
        fail_list.append(f"schoolInfo: {e}")

    try:
        await neis.mealServiceDietInfo(AE, SE1, MLSV_YMD=20200311)
    except Exception as e:
        fail_list.append(f"mealServiceDietInfo: {e}")

    try:
        await neis.SchoolSchedule(AE, SE1)
    except Exception as e:
        if e.__class__.__name__ == itsok:
            pass
        else:
            fail_list.append(f"SchoolSchedule: {e}")

    try:
        await neis.acaInsTiInfo(AE)
    except Exception as e:
        if e.__class__.__name__ == itsok:
            pass
        else:
            fail_list.append(f"acaInsTiInfo: {e}")

    try:
        await neis.timeTable("els", AE, SE1)
    except Exception as e:
        if e.__class__.__name__ == itsok:
            pass
        else:
            fail_list.append(f"timeTableELS: {e}")

    try:
        await neis.timeTable("mis", AE, SE2)
    except Exception as e:
        if e.__class__.__name__ == itsok:
            pass
        else:
            fail_list.append(f"timeTableMIS: {e}")

    try:
        await neis.timeTable("his", AE, SE3)
    except Exception as e:
        if e.__class__.__name__ == itsok:
            pass
        else:
            fail_list.append(f"timeTableHIS: {e}")

    try:
        await neis.classInfo(AE, SE1)
    except Exception as e:
        if e.__class__.__name__ == itsok:
            pass
        else:
            fail_list.append(f"classInfo: {e}")

    assert len(fail_list) == 0
