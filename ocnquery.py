from ocnutil import OcnDBManager
from ocnformat import table_db, columns_db

dbmgr = OcnDBManager()

print dbmgr.query(table_db, (('STB_NO',),), '1 = 1', None, ('STB_NO',))
