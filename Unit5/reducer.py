#!/usr/bin/env python
import os, sys

word = None
tag = None
current_word = None
current_count = 0
current_tag = None

for line in sys.stdin:
    line = line.strip()
    word, tag, count = line.split('\t', 2)

    try:
        count = int(count)
    except ValueError:
        continue

    if current_word == word and current_tag == tag:
        current_count += count
    else:
        if current_word and current_tag and current_count > 2:
            print "{2}\t{0}\t{1}".format(current_word, current_tag, current_count)
        
        current_word = word
        current_tag = tag
        current_count = count

if current_word == word and current_tag == tag and current_count > 2:
    print "{2}\t{0}\t{1}".format(current_word, current_tag, current_count)
