from __future__ import division
import nltk
from nltk.corpus import PlaintextCorpusReader


def big_event_sentences:
	corpus_root = '../Brazil_NightClub_Fire/'

	wordlists = PlaintextCorpusReader(corpus_root, '.*\.txt')

	BigEvent = wordlists.raw()

	sent_tokenizer = nltk.data.load('../nltk_data/tokenizers/punkt/english.pickle')

	BigEventSentences = nltk.data.load('../nltk_data/tokenizers/punkt/english.pickle')
	return BigEventSentences