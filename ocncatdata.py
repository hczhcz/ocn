from xml.etree import ElementTree
from ocnutil import OcnDBManager, listfile

print '==== initialize db ===='

dbmgr = OcnDBManager()

# columns_checked = []
c_attr = set()
c_title_attr = set()
c_movie_attr = set()
c_poster_attr = set()
c_title_ams = {}
c_movie_ams = {}
c_poster_ams = {}

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
    if title is not None:
        c_title_attr |= set(title.attrib)
        for i in title.getiterator('metadata'):
            if i.get('name') in c_title_ams:
                if c_title_ams[i.get('name')] < len(i.get('value')):
                    c_title_ams[i.get('name')] = len(i.get('value'))
            else:
                c_title_ams[i.get('name')] = len(i.get('value'))
    if movie is not None:
        c_movie_attr |= set(movie.attrib)
        for i in movie.getiterator('metadata'):
            if i.get('name') in c_movie_ams:
                if c_movie_ams[i.get('name')] < len(i.get('value')):
                    c_movie_ams[i.get('name')] = len(i.get('value'))
            else:
                c_movie_ams[i.get('name')] = len(i.get('value'))
    if poster is not None:
        c_poster_attr |= set(poster.attrib)
        for i in poster.getiterator('metadata'):
            if i.get('name') in c_poster_ams:
                if c_poster_ams[i.get('name')] < len(i.get('value')):
                    c_poster_ams[i.get('name')] = len(i.get('value'))
            else:
                c_poster_ams[i.get('name')] = len(i.get('value'))

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
