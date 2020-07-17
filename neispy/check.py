from .error import APIKeyNotFound


def status_info(response, querytype) -> tuple:
    try:
        datalist = response[querytype]
        headlist = datalist[0]["head"]
        code = headlist[1]["RESULT"]["CODE"]
        message = headlist[1]["RESULT"]["MESSAGE"]
        return (code, message)
    except KeyError:
        code = response["RESULT"]["CODE"]
        message = response["RESULT"]["MESSAGE"]
        return (code, message)


def check_apikey(key):
    if any(key):
        pass
    else:
        raise APIKeyNotFound()
