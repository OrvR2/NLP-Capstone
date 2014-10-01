#!/usr/bin/env python

import sys, zipimport
# from operator import itemgetter

reload(sys)
sys.setdefaultencoding('utf-8')

importer = zipimport.zipimporter('nltk.mod')
nltk = importer.load_module('nltk')
nltk.data.path += ["./nltkData/"]

stopwords_list = nltk.corpus.stopwords.words('english')
word = None
tag = None
current_word = None
curent_tag = None
current_count = 0

for line in sys.stdin:

    line = line.strip() # remove whitespace

    word, tag, count = line.split(',', 2) # splits tuple into 3 parts

    try:
        count = int(count)
    except ValueError:
        continue

    if word not in stopwords_list:
        if current_word == word and current_tag == tag:
            current_count += count
        else:
            if current_word and current_tag:
                print '{2}\t{0}\t{1}'.format(current_word, current_tag, current_count)
            current_word = word
            current_tag = tag
            current_count = count

if current_word == word:
    print '{2}\t{0}\t{1}'.format(current_word, current_tag, current_count)