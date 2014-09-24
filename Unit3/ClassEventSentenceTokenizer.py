from __future__ import division
import nltk
from nltk.corpus import PlaintextCorpusReader

def class_event_sentences():
	corpus_root = '../Islip13Rain/'

	wordlists = PlaintextCorpusReader(corpus_root, ".*\.txt")

	ClassEvent = wordlists.raw()

	sent_tokenizer = nltk.data.load('../nltkData/tokenizers/punkt/english.pickle')

	ClassEventSentences = sent_tokenizer.tokenize(ClassEvent)
	return ClassEventSentences

def small_event_sentences():
	corpus_root = '../Texas_Wild_Fire/'

	wordlists = PlaintextCorpusReader(corpus_root, '.*\.txt')

	SmallEvent = wordlists.raw()

	sent_tokenizer = nltk.data.load('../nltkData/tokenizers/punkt/english.pickle')

	SmallEventSentences = sent_tokenizer.tokenize(SmallEvent)
	return SmallEventSentences

def big_event_sentences():
	corpus_root = '../Brazil_NightClub_Fire/'

	wordlists = PlaintextCorpusReader(corpus_root, '.*\.txt')

	BigEvent = wordlists.raw()

	sent_tokenizer = nltk.data.load('../nltkData/tokenizers/punkt/english.pickle')

	BigEventSentences = sent_tokenizer.tokenize(BigEvent)
	return BigEventSentences

def main():
    sents = class_event_sentences()
    print sents

if __name__ == "__main__": main()
