# -*- coding: UTF-8 -*-

import datetime
import random
from ocnutil import OcnDBManager
from ocnformat import table_db, columns_db

dbmgr = OcnDBManager()

users = dbmgr.query(
    table_db, (('STB_NO',),),
    '1 = 1', None,
    ('STB_NO',)
)

rdata = [0] * 2880
rscale = 30

rlim = 600

for user in users:
    history = dbmgr.query(
        table_db, columns_db,
        'STB_NO = %s', user,
        ('RENTAL_TIME',)
    )

    rdata_begin = None
    rdata_end = None

    for i in history:
        # if i[-1] is None:
        #     raise 1
        if rdata_end is None:
            rdata_begin = i[-2]
            rdata_end = i[-1]
        else:
            if i[-2] - rdata_end > datetime.timedelta(0, rlim):
                seconds = (rdata_end - rdata_begin).total_seconds()

                for j in range(int(round(seconds / rscale)) + 1):
                    key = seconds / rscale * (0.9 + 0.2 * random.random())
                    rdata[int(round(key))] += 1

                rdata_begin = i[-2]
            rdata_end = i[-1]

plotdata = rdata[:len(rdata) / 4]

for i in range(len(plotdata)):
    print '{' + str(i * rscale / 60.0) + ',' + str(plotdata[i]) + '},'
