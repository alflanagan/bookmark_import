#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from collections import defaultdict, Counter

from lxml import etree as ET

PARSER = ET.HTMLParser()

def make_date_time(value):
    if isinstance(value, str):
        value = int(value)
    return time.gmtime(value)

def get_bookmark(anchor_node):
    return (anchor_node.attrib['href'],
            make_date_time(anchor_node.attrib['add_date']),
            make_date_time(anchor_node.attrib['last_modified']),
            anchor_node.text, )


def main():
    with open('data/bookmarks_20180426.html', 'r') as htmlin:
        htmldoc = ET.parse(htmlin, PARSER)
    # <html> and <body> tags are created by parser
    html = htmldoc.getroot()
    heading = ""  # gets set by <H3>, stays until next <H3>
    bookmarks = defaultdict(list)
    tag_counter = Counter()

    for kid in html.find('body').find('dl'):
        # counts[kid.tag] += 1
        if kid.tag == 'p':
            pass
        if kid.tag == 'dt':
            # if child is <H3> it's a heading
            h3tag = kid.find('h3')
            if h3tag is not None:
                heading = h3tag.text
            # if child is <A> it's a bookmark
            anchors = kid.findall('a')
            for anchor in anchors:
                bookmarks[heading].append(get_bookmark(anchor))
        if kid.tag == 'dl':
            # <DL> is a list of bookmarks with a heading given by the previous <DT><H3>
            # and/or subheadings in <DL> tags
            for node in kid:
                tag_counter[node.tag] += 1
            dts = kid.findall('dt')
            for dt in dts:
                anchors = dt.findall('a')
                for anchor in anchors:
                    bookmarks[heading].append(get_bookmark(anchor))

    for tag in tag_counter:
        print("<{}>: {:,}".format(tag, tag_counter[tag]))

    count = 0
    for key in bookmarks:
        print("{}:".format(key))
        count += len(bookmarks[key])
        for bkmk in bookmarks[key]:
            print("    {}".format(bkmk))

    print("Parse {:,} bookmarks from the file.".format(count))

if __name__ == '__main__':
    main()
