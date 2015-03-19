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


def fmtint(value):
    '''build string from an integer'''

    return str(int(value))


def fmtstr(value):
    '''call MySQLdb.string_literal'''

    return MySQLdb.string_literal(value)


def fmttype(typeinfo):
    '''convert ("char", 3) to "char(3)" or "int" to "int"'''

    if type(typeinfo) == str:
        return fmtname(typeinfo)
    else:
        return fmtname(typeinfo[0]) + '(' + ', '.join((
            fmtint(i) if type(i) == int else fmtstr(i)
            for i in typeinfo[1:]
        )) + ')'


class OcnDBManager(object):
    def __init__(
        self,
        host='localhost',
        port=3306,
        db='ocnutilpy',
        user='ocnutilpy',
        passwd='ocnutilpy',
        charset='utf8',
    ):
        '''do initialization; connect to the database'''

        self.conn = MySQLdb.connect(
            host=host,
            port=port,
            db=db,
            user=user,
            passwd=passwd,
            charset=charset,
        )
        self.cursor = self.conn.cursor()
        self.db = db

    def chktable(self, table, colname, coltype):
        '''create a table with a column if it does not exist'''

        self.cursor.execute('''
            create table if not exists `%s` (`%s` %s);
        ''' % (
            fmtname(table),
            fmtname(colname),
            fmttype(coltype),
        ))

    def chkcolumn(self, table, colname, coltype):
        '''add a column to a table if it does not exist'''

        self.cursor.execute('''
            select * from information_schema.columns
                where table_schema=%s
                    and table_name=%s
                    and column_name=%s;
        ''' % (
            fmtstr(self.db),
            fmtstr(table),
            fmtstr(colname),
        ))

        if not bool(self.cursor.fetchall()):
            # if empty
            self.cursor.execute('''
                alter table `%s` add column (`%s` %s);
            ''' % (
                fmtname(table),
                fmtname(colname),
                fmttype(coltype),
            ))

    def chkall(self, table, columns):
        '''ensure a table and its columns exist or add them'''

        self.chktable(table, columns[0][0], columns[0][1])

        for i in columns:
            self.chkcolumn(table, i[0], i[1])

    # def insert(self, table, columns, data, unique=True):
    def insert(self, table, columns, data):
        '''add rows into a table'''

        self.cursor.executemany('''
            replace into `%s` (%s) value (%s)
        ''' % (
            fmtname(table),
            ', '.join(('`' + fmtname(i[0]) + '`' for i in columns)),
            '%s, ' * (len(columns) - 1) + '%s'
        ), data)

    def __del__(self):
        '''do finalization'''

        self.conn.commit()
        self.cursor.close()
        self.conn.close()


def loadfile(path):
    '''read file as a list'''

    return open(path, 'r').readlines()


if __name__ == '__main__':
    dbmgr = OcnDBManager()

    data = [
        i.strip().split('|')
        for i in loadfile('/dev/shm/test.txt')[:100000]
        if len(i) == 181 and i[2] == ':'
    ]

    columns = (
        ('STB_NO', ('char', 17)),
        ('SERVICE_CODE', 'int'),
        ('PROVIDER', ('varchar', 64)),
        ('ASSET_NAME', ('varchar', 64)),
        ('CONTENT_NAME', ('varchar', 64)),
        ('RENTAL_TIME', 'datetime'),
        ('RENTAL_EXPIRE_TIME', 'datetime'),  # may be unavaliable
    )

    dbmgr.chkall('dbtest1', columns)
    dbmgr.insert('dbtest1', columns, data)

    # dbmgr.chktable('test1', 'c5', ('char', 123))
    # dbmgr.chkcolumn('test1', 'c3', ('char', 123))
    # dbmgr.chkcolumn('test1', 'c4', ('char', 123))
    # dbmgr.chkall('test1', (
    #     ('c1', 'int'), ('c2', ('char', 2)), ('c3', 'int')
    # ))
    # dbmgr.insert('test1', (
    #     ('c1', 'int'), ('c2', ('char', 2)), ('c3', 'int')
    # ), (
    #     (1, 2, 3), (2, 3, 4)
    # ))
    # dbmgr.insert('test1', (
    #     ('c1', 'int'), ('c3', 'int'), ('c2', ('char', 2))
    # ), (
    #     (11, 22, 33), (22, 33, 44)
    # ))
