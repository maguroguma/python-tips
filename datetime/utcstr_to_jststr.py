# -*- coding: utf-8 -*-

from datetime import datetime, timedelta, timezone


JST = timezone(timedelta(hours=+9), "JST")


def utcstr_to_jststr(utc_str: str)-> str:
    """ +9 hours """
    dt_utc = datetime.strptime(utc_str, "%Y-%m-%d %H:%M:%S")
    # dts_utc = dt_utc.timestamp()
    # dt_jst = datetime.fromtimestamp(dts_utc, JST)
    # return dt_jst.strftime("%Y-%m-%d %H:%M:%S")
    dt_utc += timedelta(hours=+9)
    return dt_utc.strftime("%Y-%m-%d %H:%M:%S")


print(utcstr_to_jststr("2019-10-25 00:00:00"))
print(utcstr_to_jststr("2019-10-25 23:59:59"))
print(utcstr_to_jststr("2019-1-25 00:00:00"))
print(utcstr_to_jststr("2019-01-25 0:0:0"))
