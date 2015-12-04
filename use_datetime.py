#use_datetime.py
# -*- coding:utf-8 -*-

import re
from datetime import datetime, timezone, timedelta


def to_timestamp(dt_str, tz_str):
    re_h=re.compile(r'\w+C([0-9+-]+):\w+')
    tz_utc = timezone(timedelta(hours=int(re_h.match(tz_str).group(1))))
    date=datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    return date.replace(tzinfo=tz_utc).timestamp()


# 测试:

t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('Pass')