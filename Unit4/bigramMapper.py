#!/usr/bin/env python

import sys, zipimport, re
reload(sys)
sys.setdefaultencoding('utf-8')
importer = zipimport.zipimporter('nltk.mod')
nltk = importer.load_module('nltk')
nltk.data.path += ["./nltkData/"]


# Tonize std.in by sentence
# input comes from STDIN (standard input)
#f = sys.stdin

sent_tokenizer = nltk.data.load('./nltkData/tokenizers/punkt/english.pickle')
t3 = nltk.data.load('./nltkData/tagger.pickle')
# got rid of f.read() so that stdin is not read multiple times
sents = sent_tokenizer.tokenize(sys.stdin.read().decode('utf-8'))

for sent in sents:
	array = re.split('\s+', sent)
	# array = sent.split(' ')
	length = len(array)
	for i in range(length):
		if (i < length - 2):
			combined = array[i].lower() + array[i+1].lower()
			print '{0}\t{1}'.format(combined, 1)
