# -*- coding: UTF-8 -*-

import sys
from xml.etree import ElementTree
from ocnutil import OcnDBManager, listfile
from ocnformat import table_cat, columns_cat, primaries_cat, map_cat

# hack
reload(sys)
sys.setdefaultencoding('utf8')

print '==== initialize db ===='

dbmgr = OcnDBManager()
dbmgr.chkall(table_cat, columns_cat, primaries_cat)

print '==== list files ===='

target = listfile('catalog/')


def loadattr(columns, data, tree, prefix):
    columns += [(prefix + map_cat[i],) for i in tree.attrib.keys()]
    data += tree.attrib.values()


def loadmeta(columns, data, tree, prefix):
    mlist = tree.getiterator('metadata')
    columns += [(prefix + i.get('name'),) for i in mlist]
    data += [i.get('value') for i in mlist]


start = 0
fin = len(target)

for path in target:
    # print '==== file: ' + path + ' ===='
    if start % 256 == 0:
        print 'Now:', start, 'Total:', fin
    start += 1

    or_none = lambda x: x if x else [None]

    alldata = ElementTree.parse(path).getiterator('offering')[0]
    description = alldata.getiterator('description')[0]
    title = or_none(alldata.getiterator('title'))[0]
    movie = or_none(alldata.getiterator('movie'))[0]
    poster = or_none(alldata.getiterator('poster'))[0]

    columns = [('DESCRIPTION',)]
    data = [description.text]

    loadattr(columns, data, alldata, '')

    if title is not None:
        loadattr(columns, data, title, 'TITLE_')
        loadmeta(columns, data, title, 'TITLE_')

    if movie is not None:
        loadattr(columns, data, movie, 'MOVIE_')
        loadmeta(columns, data, movie, 'MOVIE_')

    if poster is not None:
        loadattr(columns, data, poster, 'POSTER_')
        loadmeta(columns, data, poster, 'POSTER_')

    # print columns, data

    dbmgr.insert(table_cat, columns, (data,))
