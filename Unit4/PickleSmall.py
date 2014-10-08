#!/usr/bin/python
from __future__ import division
import nltk, pickle, random
from nltk.corpus import PlaintextCorpusReader

#train_corpus_root = '../random_small_subsets/random_small_subset'
test_corpus_root = '../Texas_Wild_Fire_Slim'

#train_corpus = PlaintextCorpusReader(train_corpus_root, '.*\.txt')
test_corpus = PlaintextCorpusReader(test_corpus_root, '.*\.txt')

pFile = open('Small_PlaintextCorpusReader.pickle', 'wb')
pickle.dump(test_corpus, pFile)
pFile.close()
