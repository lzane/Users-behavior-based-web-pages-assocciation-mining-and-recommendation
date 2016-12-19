#!/usr/bin/python

"""
Get all view pages for all individual users
Mapper: (ID,view page url)
Reducer: (user, view page urls list)
"""

import sys
import json

cnt = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something wrong. Skip this line.
        continue

    pathPair, count = data_mapped

    if oldKey and oldKey != pathPair:
        print oldKey, "\t", cnt
        cnt = 0

    oldKey = pathPair
    cnt += 1

if oldKey is not None:
    print oldKey, "\t", cnt
