#!/usr/bin/python

"""
### Recommendation
- Map: (count,similar page)
- Reduce: output Top N pages
"""

import sys

# parameter
TOPNCOUNT = 5
cnt = 0

oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something wrong. Skip this line.
        continue

    count, similar_page = data_mapped
    print similar_page, "\t", count
    cnt += 1
    if cnt == TOPNCOUNT:
        break
