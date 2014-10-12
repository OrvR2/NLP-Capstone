#!/usr/bin/env python
"""A more advanced Mapper, using Python iterators and generators."""

import sys, zipimport, os, pickle, nltk
reload(sys)
sys.setdefaultencoding('utf-8')


sfFile = open('./SmallFeatures.pickle', 'rb')
small_features = pickle.load(sfFile)
sfFile.close()

def features(document):
    document_words = set(document)
    features = {}
    for word in small_features:
        features['contains(%s)' % word] = (word in document_words)
    return features
'''
# Because the pickled classifier incorrectly labels each text as neg,
# we are forced to train the classifier in the mapper.
train_corpus_root = '../training_set'
train_corpus = nltk.corpus.PlaintextCorpusReader(train_corpus_root, '.*\.txt')
train_documents = [(list(train_corpus.words(fileid)), fileid[-7:-4])
                      for fileid in train_corpus.fileids()]

featuresets = [(features(d), c) for (d, c) in train_documents]
train_set = featuresets
classifier = nltk.NaiveBayesClassifier.train(train_set)
'''

cFile = open('./MaxentClassifier.pickle', 'rb')
classifier = pickle.load(cFile)
cFile.close()

cachedir = '../Texas_Wild_Fire_Slim'

count = 0

for fileName in sys.stdin:
    if count > 1000:
	break
    count += 1
    fileName = fileName.strip()
    aFileName = os.path.join(cachedir, fileName)
    file = open(aFileName, 'r')    
    result = classifier.classify(features(file))
    file.close()
    
    print "{0}\t{1}".format(fileName, result)
