# -*- coding: utf-8 -*-

from datetime import datetime, timedelta, timezone


def clean_30_minutes(datetime_string: str)-> datetime:
    """ round down 30 minutes """
    d = datetime.strptime(datetime_string, '%Y-%m-%d %H:%M:%S')   # datetime
    dt = d.timestamp()    # timestamp
    dt = int(dt) - (int(dt) % 1800)   # 30分区切りにする
    cd = datetime.fromtimestamp(dt)
    # return cd.strftime('%Y-%m-%d %H:%M:%S')
    return cd

print(
    clean_30_minutes(
        datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    ) - timedelta(minutes=30)
)
print(clean_30_minutes(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')))
print("---")
print(clean_30_minutes('2019-09-18 00:00:00') - timedelta(minutes=30))
print(clean_30_minutes('2019-09-18 00:00:00'))
print(clean_30_minutes('2019-09-18 00:00:01') - timedelta(minutes=30))
print(clean_30_minutes('2019-09-18 00:00:01'))
print(clean_30_minutes('2019-09-18 00:15:00') - timedelta(minutes=30))
print(clean_30_minutes('2019-09-18 00:15:00'))
print(clean_30_minutes('2019-09-18 00:29:59') - timedelta(minutes=30))
print(clean_30_minutes('2019-09-18 00:29:59'))
print(clean_30_minutes('2019-09-18 00:30:00') - timedelta(minutes=30))
print(clean_30_minutes('2019-09-18 00:30:00'))
print(clean_30_minutes('2019-09-18 00:30:01') - timedelta(minutes=30))
print(clean_30_minutes('2019-09-18 00:30:01'))
print(clean_30_minutes('2019-09-18 00:45:00') - timedelta(minutes=30))
print(clean_30_minutes('2019-09-18 00:45:00'))
print(clean_30_minutes('2019-09-18 00:59:59') - timedelta(minutes=30))
print(clean_30_minutes('2019-09-18 00:59:59'))

print(type(clean_30_minutes('2019-09-18 00:00:00')))
print(type(clean_30_minutes('2019-09-18 00:00:01')))
print(type(clean_30_minutes('2019-09-18 00:15:00')))
print(type(clean_30_minutes('2019-09-18 00:29:59')))
print(type(clean_30_minutes('2019-09-18 00:30:00')))
print(type(clean_30_minutes('2019-09-18 00:30:01')))
print(type(clean_30_minutes('2019-09-18 00:45:00')))
print(type(clean_30_minutes('2019-09-18 00:59:59')))


def _round_down_30_minutes(dt: datetime)-> datetime:
    """30分を超える部分を丸める"""
    dt_timestamp = dt.timestamp()
    dt_timestamp = int(dt_timestamp) - (int(dt_timestamp) % 1800)
    return datetime.fromtimestamp(dt_timestamp)

print(_round_down_30_minutes(datetime.utcnow()) - timedelta(minutes=30))
print(_round_down_30_minutes(datetime.utcnow()))

# utcnowから一気にJSTの自然言語形式へ
print("utcnowから一気にJSTの自然言語形式へ（謎）")
now_timestamp = int(datetime.utcnow().timestamp())
print(
    datetime.fromtimestamp(
        datetime.utcnow().timestamp(), timezone(timedelta(hours=+9), 'JST')
    ).strftime("%Y-%m-%d %H:%M:%S"),
    datetime.fromtimestamp(datetime.utcnow().timestamp())
)
print(
    datetime.fromtimestamp(
        now_timestamp, timezone(timedelta(hours=+9), 'JST')
    ).strftime("%Y-%m-%d %H:%M:%S"),
    datetime.fromtimestamp(now_timestamp).strftime("%Y-%m-%d %H:%M:%S"),
    datetime.fromtimestamp(now_timestamp + 9*3600).strftime("%Y-%m-%d %H:%M:%S")
)

print("文字列定数でタイムゾーンを指定")
_ts = 1568922742
ts = _ts - (_ts % 60)
utc_dt = datetime.fromtimestamp(ts, timezone(timedelta(hours=+0), 'UTC'))
jst_dt = datetime.fromtimestamp(ts, timezone(timedelta(hours=+9), 'Asia/Tokyo'))
print(utc_dt.strftime("%Y-%m-%d %H:%M:%S"), jst_dt.strftime("%Y-%m-%d %H:%M:%S"))
print(datetime.fromtimestamp(ts))
print(datetime.fromtimestamp(ts + 9*3600))

JST = timezone(timedelta(hours=+9), 'JST')
print(datetime.now(JST).strftime("%Y-%m-%d %H:%M:%S"))