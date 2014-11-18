#!/usr/bin/env python
import sys, os, re

result = None
attribute = None
current_result = None
current_count = 0
current_attribute = None

for line in sys.stdin:
    line = line.strip()
    attribute, count, result = line.split(';', 2)

    try:
        count = int(count)
    except ValueError:
        continue

    if current_result == result:
        current_count += count
    else:
        if current_result and current_attribute and current_count > 2:
            print "{0}\t{1}\t{2}".format(current_attribute, current_count, current_result)
        
        current_result = result
        current_attribute = attribute
        current_count = count

if current_result == result and current_count > 2:
    print "{0}\t{1}\t{2}".format(current_attribute, current_count, current_result)
