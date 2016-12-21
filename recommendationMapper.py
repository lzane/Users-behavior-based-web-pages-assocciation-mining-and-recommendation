#!/usr/bin/python

"""
### Recommendation
- Map: `(pageA '\t' count,pageB)`
- Reduce: Top-N `(page, similar page array[{url,count},...])`
"""

import sys
import json

for line in sys.stdin:
    line = line.strip().split('\t')
    if len(line) != 2:  # something wrong, ignore
        continue
    urlListJson, count = line
    count = int(count)
    urlList = json.loads(urlListJson)
    if len(urlList) != 2:  # something wrong, ignore
        continue

    print "{0}\t{1}".format(urlList[0], json.dumps({"url": urlList[1], "count": count}))
    print "{0}\t{1}".format(urlList[1], json.dumps({"url": urlList[0], "count": count}))
