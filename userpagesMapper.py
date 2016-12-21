#!/usr/bin/python

"""
Get all view pages for all individual users
Mapper: (ID,view page url)
Reducer: (user, view page urls list)
"""

import re
import sys

p = re.compile(
    r'([^ ]*)\s([^ ]*)\s([^ ]*)\s\[([^\]]*)\]\s\"([^\"]*)\"\s(\d*)\s(\d*)'
)

for line in sys.stdin:
    line = line.strip()
    m = p.match(line)
    if not m:  # do not match the log format
        continue
    res = m.groups()
    IP, identity, username, time, request, status, size = res
    request = request.split(' ')
    if len(request) != 3:  # something wrong happens
        continue
    path = request[1]
    if path.split('.')[-1] != "html":  # only concentrate on html, ignore css,image etc
        continue
    print "{0}\t{1}".format(IP, path)
