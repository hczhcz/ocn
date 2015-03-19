# import os, time, xml
import string
import MySQLdb


def fmtname(name):
    '''check a string; allow letters, digits and underlines only'''

    charset = string.ascii_letters + string.digits + '_'
    for i in name:
        if i not in charset:
            raise Exception('bad id: ' + name)

    return name

def fmttype(name):
    '''convert ("char", 3) to "char(3)" or "int" to "int"'''

    if type(name) == str:
        return fmtname(name)
    else:
        return fmtname(name[0]) + '(' + str(int(name[1])) + ')'


class OcnDBTask(object):
    def __init__(
        self,
        host='localhost',
        port=3306,
        db='ocnutilpy',
        user='ocnutilpy',
        passwd='ocnutilpy',
        table='data',
        charset='utf8',
    ):
        self.conn = MySQLdb.connect(
            host=host,
            port=port,
            db=db,
            user=user,
            passwd=passwd,
            charset=charset,
        )
        self.cursor = self.conn.cursor()
        self.table = table

    def chktable(self, colname, coltype):
        '''create a table with a column if it does not exist'''

        self.cursor.execute('''
            create table if not exists %s(%s %s);
        ''' % (
            fmtname(self.table),
            fmtname(colname),
            fmttype(coltype),
        ))

    def chkcol(self, colname, coltype):
        pass

    def __del__(self):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()


# class OcnDBLoadTask(OcnDBTask):
#     def __init__():
#         super(OcnDBTask, self)


def loadfile(path):
    '''read file as a string'''
    return open(path, 'r').read()


if __name__ == '__main__':
    task = OcnDBTask(table='test1')
    task.chktable('col1', ('char', 123))
