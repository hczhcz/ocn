from xml.etree import ElementTree
from ocnutil import OcnDBManager, listfile

print '==== initialize db ===='

dbmgr = OcnDBManager()

# columns_checked = []
c_attr = set()
c_title_attr = set()
c_movie_attr = set()
c_poster_attr = set()
c_title_ams = set()
c_movie_ams = set()
c_poster_ams = set()

print '==== list files ===='

target = listfile('catalog/')

# xset = set()

for path in target:
    print '==== file: ' + path + ' ===='

    or_none = lambda x: x if x else [None]

    alldata = ElementTree.parse(path).getiterator('offering')[0]
    description = alldata.getiterator('description')[0]
    title = or_none(alldata.getiterator('title'))[0]
    movie = or_none(alldata.getiterator('movie'))[0]
    poster = or_none(alldata.getiterator('poster'))[0]

    c_attr |= set(alldata.attrib)
    if title:
        c_title_attr |= set(title.attrib)
        c_title_ams |= {i.get('name') for i in title.getiterator('metadata')}
    if movie:
        c_movie_attr |= set(movie.attrib)
        c_movie_ams |= {i.get('name') for i in movie.getiterator('metadata')}
    if poster:
        c_poster_attr |= set(poster.attrib)
        c_poster_ams |= {i.get('name') for i in poster.getiterator('metadata')}

    print c_attr
    print c_title_attr
    print c_movie_attr
    print c_poster_attr
    print c_title_ams
    print c_movie_ams
    print c_poster_ams


    # print alldata.attrib
    # print description.text
    # if title:
    #     print title.attrib
    #     print [i.attrib for i in title.getiterator('metadata')]
    # if movie:
    #     print movie.attrib
    # if poster:
    #     print poster.attrib

    # for i in alldata.getchildren():
    #     print i.tag
    #     xset.add(i.tag)
    #     print xset
    #print alldata.getiterator('movies')
