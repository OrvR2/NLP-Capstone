#!/usr/bin/python
# http://collabedit.com/tpd35

import nltk
from nltk import *
from nltk.corpus import PlaintextCorpusReader
import random
import re

print 'creating small reader'
corpus_root = 'NLP-Capstone/random_small_subsets/combined_subset'
yourSmallReader = PlaintextCorpusReader(corpus_root, '.*')

print 'creating FreqDist'
all_words = nltk.FreqDist(w.lower() for w in yourSmallReader.words())
word_features = all_words.keys()[:2000]

print 'creating documents'
documents = {}
for fileid in yourSmallReader.fileids():
    documents[fileid] = list(yourSmallReader.words(fileid))

# print 'shuffling documents'
# random.shuffle(documents)

def document_features(document):
    document_words = set(document)
    features = {}
    # print 'creating features'
    for word in word_features:
        if len(word) > 3:
            # print 'word = ', word
            features['contains(%s)' % word.strip()] = (word in document_words)
    return features

# print document_features(yourSmallReader.words('1.txt'))

print 'creating featuresets'
featuresets = [(document_features(documents[fileid]), fileid[-8:] == '_pos.txt') for fileid in documents]

print 'making training and testing sets'
train_set, test_set = featuresets, featuresets[130:]

print 'making classifier'
classifier = nltk.NaiveBayesClassifier.train(train_set)

print 'showing most show_most_informative_features'
classifier.show_most_informative_features(1000)

print 'Getting accuracy of these featuresets'
print 'Accuracy = ', nltk.classify.accuracy(classifier, test_set)
