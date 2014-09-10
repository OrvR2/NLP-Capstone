from __future__ import division
import nltk
#nltk.download()
#from nltk.book import *
import nltk.corpus
#from nltk.corpus import PlaintextCorpusReader
import dateutil
import pyparsing
import numpy
import six
import matplotlib
from nltk.corpus import PlaintextCorpusReader
corpus_root = '/Users/mzamani/Documents/CS4984/Unit1/Islip13Rain'
wordlists = PlaintextCorpusReader(corpus_root, '.*\.txt')
# The next step is to show the file names under the directory (optional step)
print wordlists.fileids()

ClassEvent = nltk.Text(wordlists.words())