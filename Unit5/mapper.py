#!/usr/bin/env python
import sys, zipimport, os

java_path = "/usr/bin/java"
os.environ['JAVAHOME'] = java_path

importer = zipimport.zipimporter('nltk.mod')
nltk = importer.load_module('nltk')
nltk.data.path += ["./nltkData/"]

f = sys.stdin

tagger = nltk.tag.stanford.NERTagger('./nltkData/english.all.3class.distsim.crf.ser.gz', './nltkData/stanford-ner.jar') 

event_dir = './event'

# Each line in sys.stdin will be the name of a document.
for line in f.readlines():
    line = line.strip()
    filePath = os.path.join(event_dir, line)
    file = open(filePath, 'r')
    words = file.read()
    file.close()

    words = nltk.tokenize.word_tokenize(words)

    words = [w.encode('utf8', 'ignore') for w in words if len(w.strip()) > 3 and w.isalpha()]

    named_entities = tagger.tag(words)

    for word, tag in named_entities:
        if tag != 'O':
            print "{0}\t{1}\t{2}".format(word, tag, 1)
