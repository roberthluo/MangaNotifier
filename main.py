
# Import Custom libraries
from feedgen.feed import FeedGenerator
from BeautifulSoup import BeautifulSoup, BeautifulStoneSoup, Tag, NavigableString, CData

def gen_xml(record):

    description_blank_str = \
    '''
    <item>
    <title>Entry Title</title>
    <link>Link to the entry</link>
    <guid>http://example.com/item/123</guid>
    <pubDate>Sat, 9 Jan 2016 16:23:41 GMT</pubDate>
    <description>[CDATA[ This is the description. ]]</description>
    </item>
    '''
    description_xml_tag = BeautifulStoneSoup(description_blank_str)

    key_pair_locations = \
    [
        ("title", lambda x: x.name == u"title"),
        ("link", lambda x: x.name == u"link"),
        ("guid", lambda x: x.name == u"guid"),
        ("author", lambda x: x.name == u"author"),
        ("pubDate", lambda x: x.name == u"pubdate"),
        ("description", lambda x: x.name == u"description")
    ]

    tmp_description_tag_handle = deepcopy(description_xml_tag)

    for (key, location) in key_pair_locations:
        search_list = tmp_description_tag_handle.findAll(location)
        if(not search_list):
            continue
        tag_handle = search_list[0]
        tag_handle.clear()
        if(key == "description"):
            tag_handle.insert(0, CData(record[key]))
        else:
            tag_handle.insert(0, record[key])

    return tmp_description_tag_handle

