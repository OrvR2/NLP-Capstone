#!/usr/bin/env python
import nltk, sys, zipimport, os, TextUtils 

java_path = "/usr/bin/java"
os.environ['JAVAHOME'] = java_path

importer = zipimport.zipimporter('nltk.mod')
nltk = importer.load_module('nltk')
nltk.data.path += ["./nltkData/"]

event_dir = '../Islip13Rain/'

# Path below is specifically for local. Change for Mapper.
tagger = nltk.tag.stanford.NERTagger('./stanford-ner-2014-08-27/classifiers/english.all.3class.distsim.crf.ser.gz', './stanford-ner-2014-08-27/stanford-ner.jar') 

# Each line in sys.stdin will be the name of a document.
for line in sys.stdin:
    line = line.strip()
    word_list = nltk.corpus.PlaintextCorpusReader(event_dir, line, encoding="utf8")
    words = [w.encode('utf8', 'ignore') for w in word_list.words() if len(w.strip()) > 3 and TextUtils.is_ascii(w) and w.isalpha()]

    line = line.strip()
    file_path = os.path.join(class_event_dir, line)
    document = open(file_path, 'r')
    # sents = nltk.sent_tokenize(document.read().decode('utf-8'))
    document.close()

    named_entities = tagger.tag(words)
    for word, tag in named_entities:
         if tag != 'O':
             print "{0}\t{1}\t{2}".format(word, tag, 1)
