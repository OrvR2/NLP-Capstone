#!/usr/bin/env python

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
sents = sent_tokenizer.tokenize(f.read().decode('utf-8'))

for sent in sents:
    length = len(sent)
    for i in range(length):
        if (i < length - 1):
        	print '{0},{1},{2}'.format(sent[i].lower(), sent[i+1].lower(), 1)