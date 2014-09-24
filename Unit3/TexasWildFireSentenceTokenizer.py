from __future__ import division
import nltk
from nltk.corpus import PlaintextCorpusReader

def small_event_sentences:
	corpus_root = '../Texas_Wild_Fire/'

	wordlists = PlaintextCorpusReader(corpus_root, '.*\.txt')

	SmallEvent = wordlists.raw()

	sent_tokenizer = nltk.data.load('../nltk_data/tokenizers/punkt/english.pickle')

	SmallEventSentences = sent_tokenizer.tokenize(SmallEvent)
	return SmallEventSentences