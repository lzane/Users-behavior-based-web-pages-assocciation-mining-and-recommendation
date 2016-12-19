#!/usr/bin/python

"""
Mining Association rules
Mapper:((page1,page2),1)
Reducer: ((page1,page2),count)
!!guarantee page1<page2!!
"""

import sys
import json

for line in sys.stdin:
    line = line.strip().split('\t')
    if len(line) != 2:  # something wrong, ignore
        continue
    urlListJson = line[1]
    urlList = json.loads(urlListJson)
    if len(urlList) <= 1:  # only one page url
        continue

    for i in range(len(urlList)):
        for j in range(i + 1, len(urlList)):
            urlA = urlList[i]
            urlB = urlList[j]
            if urlB < urlA:  # !!guarantee page1<page2!!
                temp = urlA
                urlA = urlB
                urlB = temp
            print "{0}\t{1}".format(json.dumps([urlA, urlB]), 1)
