from __future__ import nltk
import nltk
import os

current_directory = os.path.dirname(__file__)
corpus_root = os.path.abspath(current_directory)
ClassEvent = nltk.PlaintextCorpusReader(corpus_root, "/Islip13Rain/.*\.txt")

# Part of Speech Tagging.

fdist = nltk.FreqDist(ClassEvent)

word_list = ClassEvent.words()

stopwords = nltk.corpus.stopwords.words('english')
word_list = [w.lower() for w in word_list if w.lower() not in stopwords]


print word_list[:40]