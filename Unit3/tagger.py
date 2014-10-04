#BrownAndTreebankTagsList.py - by Tarek Kanan, 9/15/2014, for VT CS4984, CL
from __future__ import division
import nltk, pickle
from nltk.corpus import brown
from nltk.corpus import treebank

# Building a large tagging corpus(FireEventTrainingSet) by combining
#  the Brown and Reuters POS tagging corpora.
FireEventTrainingSet = nltk.corpus.brown.tagged_words() + nltk.corpus.treebank.tagged_words()
fire = brown.words() + treebank.words()

#To print the number of POS tags in the new big tags corpus

#print 'the number of tags in the corpus: ', len(FireEventTrainingSet)

#To print the new corpus tags list
#print '\n the corpus tags list', FireEventTrainingSet

>>>>>>> Unit 4 files. Subsets for manual classification
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
#bigram_tagger.tag(_sents)

# tagging
t0 = nltk.DefaultTagger('JJ')
t1 = nltk.UnigramTagger(train_sents, backoff=t0)
t2 = nltk.BigramTagger(train_sents, backoff=t1)
t3 = nltk.TrigramTagger(train_sents, backoff=t2)

print t3

pickle_name = "tagger.pickle"
pickle_object = open(pickle_name, 'wb')
pickle.dump(t3, pickle_object)
pickle_object.close()


pickle_object = open(pickle_name, 'r')
p = pickle.load(pickle_object)
print p
