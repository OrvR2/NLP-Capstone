""" Word and named entity 10 chunks """

import nltk
from nltk.corpus import PlaintextCorpusReader
import pickle

print 'getting files'
corpus_root = 'Texas_Wild_Fire'
english = pickle.load(open('./nltk_data/tokenizers/punkt/english.pickle', 'r'))
yourSmallReader = PlaintextCorpusReader(corpus_root, '.*', sent_tokenizer=english)

print 'getting sentences'
# 10324.txt 17749.txt 17859.txt
sents = yourSmallReader.sents('10324.txt') + yourSmallReader.sents('17749.txt') + yourSmallReader.sents('17859.txt')
# sents = yourSmallReader.sents()
sents = [nltk.pos_tag(sent) for sent in sents]

print 'getting chunks'
chunks = [nltk.ne_chunk(sent) for sent in sents]

# Getting a random assortment of chunks
print chunks[0]
print chunks[10]
print chunks[25]
print chunks[35]
print chunks[50]
print chunks[60]
print chunks[75]
print chunks[80]
print chunks[90]
print chunks[100]



