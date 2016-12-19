#!/usr/bin/python

"""
Get all view pages for all individual users
Mapper: (ID,view page url)
Reducer: (user, view page urls list)
"""

import sys
import json

urlList = list()
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something wrong. Skip this line.
        continue

    ID, path = data_mapped

    if oldKey and oldKey != ID:
        print oldKey, "\t", json.dumps(urlList)
        cnt = 0

    oldKey = ID
    urlList.append(path)

if oldKey is not None:
    print oldKey, "\t", json.dumps(urlList)
