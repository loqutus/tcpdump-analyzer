#!/usr/bin/env python3
import sys
import json
request_types = {}
domains = {}
try:
    sys.argv[1]
except IndexError:
    input_request_type = 'A'
else:
    input_request_type = sys.argv[1]
with open('dump.txt') as f:
    for line in f:
        if '>' in line:
            split = line.split()
            if 'domain' in split[2]:
                request_type = split[4][:-1]
                domain = split[5][:-1]
                if request_type not in request_types:
                    request_types[request_type] = 1
                else:
                    request_types[request_type] += 1
                if domain not in domains:
                    domains[domain] = 1
                else:
                    domains[domain] += 1
with open('output.txt', 'wb') as f:
    f.write(json.dumps(request_types).encode('utf-8'))
    f.write(json.dumps(domains).encode('utf-8'))
