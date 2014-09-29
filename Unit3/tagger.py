#BrownAndTreebankTagsList.py - by Tarek Kanan, 9/15/2014, for VT CS4984, CL
from __future__ import division
import nltk
from nltk.corpus import brown
from nltk.corpus import treebank
import pickle

brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')

unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)
unigram_tagger.tag(brown_sents[2007])

size = int(len(brown_tagged_sents) * 0.9)
train_sents = brown_tagged_sents[:size]
test_sents = brown_tagged_sents[size:]

unigram_tagger = nltk.UnigramTagger(train_sents)
unigram_tagger.evaluate(test_sents)

bigram_tagger = nltk.BigramTagger(train_sents)
bigram_tagger.tag(brown_sents[2007])

unseen_sent = brown_sents[4203]


# tagging
t0 = nltk.DefaultTagger('NN')
t1 = nltk.UnigramTagger(train_sents, backoff=t0)
t2 = nltk.BigramTagger(train_sents, backoff=t1)
t3 = nltk.TrigramTagger(train_sents, backoff=t2)

pickle_name = "tagger"
pickle_object = open(pickle_name, 'wb')
pickle.dump(t3, pickle_object)
pickle_object.close()

t3.tag(unseen_sent)
