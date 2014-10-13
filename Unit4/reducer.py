#!/usr/bin/env python

import sys, zipimport
# from operator import itemgetter

reload(sys)
sys.setdefaultencoding('utf-8')

importer = zipimport.zipimporter('nltk.mod')
nltk = importer.load_module('nltk')
nltk.data.path += ["./nltkData/"]

word = None
result = None

for line in sys.stdin:
    #if line.endswith('pos'):
    print line
