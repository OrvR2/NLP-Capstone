#!/usr/bin/env python
"""A more advanced Mapper, using Python iterators and generators."""

import sys, zipimport
reload(sys)
sys.setdefaultencoding('utf-8')
importer = zipimport.zipimporter('nltk.mod')
nltk = importer.load_module('nltk')
nltk.data.path += ["./nltkData/"]


# Tonize std.in by sentence
# input comes from STDIN (standard input)
f = sys.stdin

sent_tokenizer = nltk.data.load('./nltkData/tokenizers/punkt/english.pickle')
t3 = nltk.data.load('./nltkData/tagger.pickle')
sents = sent_tokenizer.tokenize(f.read().encode('utf-8'))

for sent in sents:
    
    taggedWords = t3.tag(nltk.word_tokenize(sent))
        
    for word in taggedWords:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        isnoun = word[1][0] == 'N'
        print '{0},{1},{2}'.format(word[0].decode('utf-8'), 1, isnoun)
