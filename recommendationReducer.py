#!/usr/bin/python

"""
### Recommendation
- Map: `(pageA '\t' count,pageB)`
- Reduce: Top-N `(page, similar page array[{url,count},...])`
"""

import sys
import json
from operator import itemgetter

# parameter
TOPNCOUNT = 3

oldKey = None
urlList = list()

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something wrong. Skip this line.
        continue

    target_page, similar_page = data_mapped
    similar_page = json.loads(similar_page)

    if not similar_page and len(similar_page[0]) != 1:  # Something wrong. Skip this line.
        continue

    if oldKey and oldKey != target_page:
        urlList = sorted(urlList, key=itemgetter('count'), reverse=True)
        max_index = min(TOPNCOUNT, len(urlList))
        print oldKey, "\t", json.dumps(urlList[:max_index])
        del urlList[:]

    oldKey = target_page
    urlList.append(similar_page)

if oldKey is not None:
    urlList = sorted(urlList, key=itemgetter('count'), reverse=True)
    max_index = min(TOPNCOUNT, len(urlList))
    print oldKey, "\t", json.dumps(urlList[:max_index])
    del urlList[:]

