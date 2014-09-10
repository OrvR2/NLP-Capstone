from __future__ import division
import nltk
#nltk.download()
#from nltk.book import *
import dateutil
import pyparsing
import numpy
import six
import matplotlib
from nltk.corpus import PlaintextCorpusReader
import os

def non_stopword_fraction(collection):
	stopwords = nltk.corpus.stopwords.words('english')
	list_of_non_stopwords = [w for w in collection if w.lower() not in stopwords]
	return len(list_of_non_stopwords) / len(collection)

def word_length_distributions(collection):
	print "ClassEvent % in 1-15", words_in_length_range(collection, 1, 15)
	print "ClassEvent % in 1-3", words_in_length_range(collection, 1, 3)
	print "ClassEvent % in 4-8", words_in_length_range(collection, 4, 8)
	print "ClassEvent % in 9-15", words_in_length_range(collection, 9, 15)

def words_in_length_range(collection, low, high):
	list_of_words_in_range = [w for w in collection if
		len(w) >= low and len(w) <= high]
	return len(list_of_words_in_range) / len(collection)

def print_percentage_of_word_in_collection(collection, word_list):
	fdist = nltk.FreqDist(collection)
	for word in word_list:
		if " " in word:
			# Count the frequency of bigrams somehow.
			pass
		else:
			print fdist[word] / len(collection)

def main():
	current_directory = os.path.dirname(__file__)
	corpus_root = os.path.abspath(current_directory)
	wordlists = PlaintextCorpusReader(corpus_root, 'Islip13Rain/.*\.txt')
	wordlists.fileids()
	ClassEvent = nltk.Text(wordlists.words())
	CEWords = ["Long Island", "Weather Service", "flooding", "August", 
		"heavy rains", "Wednesday", "Suffolk County", "New York", "rainfall",
		"record"]


	wordlists_event = PlaintextCorpusReader(corpus_root, "Texas_Wild_Fire/.*\.txt")
	wordlists_event.fileids()
	YourSmall = nltk.Text(wordlists_event.words())

	# ClassEvent Statistics
	print "ClassEvent non stopwords", non_stopword_fraction(ClassEvent)	
	print_percentage_of_word_in_collection(ClassEvent, CEWords)

	# YourSmall statistics
	print "Texas_Wild_Fire", non_stopword_fraction(YourSmall)

if __name__ == "__main__": main()