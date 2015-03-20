from ocnutil import *

dbmgr = OcnDBManager()

data = [
    i.strip().split('|')
    for i in loadfile('/dev/shm/test.txt')
    if len(i) == 181 and i[2] == ':'
]

# fix
for i in data:
    if i[6] == '':
        i[6] = i[5]

columns1 = (
    ('STB_NO', ('char', 17)),
    ('SERVICE_CODE', 'int'),
    ('PROVIDER', ('varchar', 64)),
    ('ASSET_NAME', ('varchar', 64)),
    ('CONTENT_NAME', ('varchar', 64)),
    ('RENTAL_TIME', 'datetime'),
    ('RENTAL_EXPIRE_TIME', 'datetime'),  # may be unavaliable
)

primaries1 = (
    'STB_NO',
    # 'SERVICE_CODE', 'PROVIDER',
    # 'ASSET_NAME', 'CONTENT_NAME',
    'RENTAL_TIME', 'RENTAL_EXPIRE_TIME'
)

dbmgr.chkall('dbtest1', columns1, primaries1)

dbmgr.insertmany('dbtest1', columns1, data)
