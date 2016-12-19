#!/usr/bin/python

"""
### Recommendation
- Map: (count,similar page)
- Reduce: output Top N pages
"""

import sys
import json

# parameters:
targetUrl = "/shuttle/countdown/countdown.html"


def find_target(urlA, urlB, innerCount):
    if urlA == targetUrl:
        print "{0}\t{1}".format(innerCount, urlB)


for line in sys.stdin:
    line = line.strip().split('\t')
    if len(line) != 2:  # something wrong, ignore
        continue
    urlListJson, count = line
    urlList = json.loads(urlListJson)
    if len(urlList) != 2:  # something wrong, ignore
        continue

    find_target(urlList[0], urlList[1], count)
    find_target(urlList[1], urlList[0], count)
