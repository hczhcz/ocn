from ocnutil import OcnDBManager, loadfile, listfile
from ocnformat import table_db, columns_db, primaries_db

print '==== initialize db ===='

dbmgr = OcnDBManager()
dbmgr.chkall(table_db, columns_db, primaries_db)

print '==== list files ===='

target = (
    listfile('20130101-0109/')
    + listfile('20130110-0116/')
)

for path in target:
    print '==== file: ' + path + ' ===='

    # path = '/dev/shm/test.txt'
    data = [
        i.strip().split('|')
        for i in loadfile(path)
        if len(i) == 181 and i[2] == ':' and i[15] + i[16] == '00'
    ]

    # fix
    for i in data:
        if i[6] == '':
            i[6] = i[5]

    dbmgr.insertmany(table_db, columns_db, data)
