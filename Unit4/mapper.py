#!/usr/bin/env python
"""A more advanced Mapper, using Python iterators and generators."""

import sys, zipimport, os, pickle
reload(sys)
sys.setdefaultencoding('utf-8')
importer = zipimport.zipimporter('nltk.mod')
nltk = importer.load_module('nltk')
nltk.data.path += ["./nltkData/"]

lfFile = open('./nltkData/LargeFeatures.pickle', 'rb')
large_features = pickle.load(lfFile)
lfFile.close()

def features(document):
    document_words = set(document)
    features = {}
    for word in large_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

train_corpus_root = './train'
train_corpus = nltk.corpus.PlaintextCorpusReader(train_corpus_root, '.*\.txt')
train_documents = [(list(train_corpus.words(fileid)), fileid[-7:-4])
                      for fileid in train_corpus.fileids()]

featuresets = [(features(d), c) for (d, c) in train_documents]
train_set = featuresets
classifier = nltk.NaiveBayesClassifier.train(train_set)

''' Not working. Classifier classifies everything as neg.
cFile = open('./nltkData/DecisionTreeClassifier.pickle', 'rb')
classifier = pickle.load(cFile)
cFile.close()

classifier = nltk.data.load('./nltkData/NaiveBayesClassifier.pickle')
'''

cachedir = 'large_slim/'

for fileName in sys.stdin:
    fileName = fileName.strip()
    numDiscard, fileName = fileName.split()
    aFileName = os.path.join(cachedir, fileName)
    file = open(aFileName, 'r')
    fileWords = nltk.word_tokenize(file.read().decode('utf-8'))    
    result = classifier.classify(features(fileWords))
    file.close()
    
    print "{0}\t{1}".format(fileName, result)
