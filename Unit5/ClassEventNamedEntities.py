#!/usr/bin/env python
from __future__ import division
import nltk, sys, zipimport, os 
reload(sys)
sys.setdefaultencoding('utf-8')
'''
importer = zipimport.zipimporter('nltk.mod')
nltk = importer.load_module('nltk')
nltk.data.path += ["./nltkData/"]
'''
class_event_dir = '../Islip13Rain/'

# Path below is specifically for local. Change for Mapper.
sent_tokenizer = nltk.data.load('../nltk_data/tokenizers/punkt/english.pickle') 
tagger = nltk.tag.stanford.NERTagger('./stanford-ner-2014-08-27/classifiers/english.all.3class.distsim.crf.ser.gz', './stanford-ner-2014-08-27/stanford-ner.jar') 

# Each line in sys.stdin will be the name of a document.
for line in sys.stdin:
    line = line.strip()
    file_path = os.path.join(class_event_dir, line)
    document = open(file_path, 'r')
    sents = sent_tokenizer.tokenize(document.read().decode('utf-8'))
    document.close()
    
    for sent in sents:
	# Filters all non-ascii characters to avoid errors.
        sent = ''.join([i if ord(i) < 128 else ' ' for i in sent]) 
        chunk = tagger.tag(sent.split())
	for word, tag in chunk:
	    if tag != 'O':
                 print "{0}\t{1}\t{2}".format(word, tag, 1)
