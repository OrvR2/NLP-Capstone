#!/usr/bin/python
from __future__ import division
import nltk, pickle, random
from sklearn.svm import SVC
from nltk.corpus import PlaintextCorpusReader

train_corpus_root = '../random_small_subsets/combined_subset'
test_corpus_root = '../Texas_Wild_Fire_Slim'

train_corpus = PlaintextCorpusReader(train_corpus_root, '.*\.txt')

test_corpus = PlaintextCorpusReader(test_corpus_root, '.*\.txt')

small_features = None

train_documents = [(list(train_corpus.words(fileid)), fileid[-7:-4])
		      for fileid in train_corpus.fileids()]

#test_documents = [list(test_corpus.words(fileid)) for
#		      fileid in test_corpus.fileids()]

random.shuffle(train_documents)

with open('SmallFeatures.pickle', 'rb') as file:
    small_features = pickle.load(file)

def texas_wild_fire_features(document):
    document_words = set(document)
    features = {}
    for word in small_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

featuresets = [(texas_wild_fire_features(d), c) for (d, c) in train_documents]
train_set, test_set = featuresets[50:], featuresets[:50]
classifier = nltk.classify.SklearnClassifier(SVC())
classifier.train(train_set)

print '\n', nltk.classify.accuracy(classifier, test_set), '\n'

# classifier.show_most_informative_features(25)

'''
for i in range(1, 10):
    print classifier.classify(texas_wild_fire_features(test_documents[i])) 
'''
