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

def print_word_length_distributions(collection):
	print "ClassEvent % in 1-15:", word_length_distribution(collection, 1, 15)
	print "ClassEvent % in 1-3:", word_length_distribution(collection, 1, 3)
	print "ClassEvent % in 4-8:", word_length_distribution(collection, 4, 8)
	print "ClassEvent % in 9-15:", word_length_distribution(collection, 9, 15)

def word_length_distribution(collection, low, high):
	list_of_words_in_range = [w for w in collection if
		len(w) >= low and len(w) <= high]
	return len(list_of_words_in_range) / len(collection)

def print_percentage_of_word_in_collection(collection, word_list):
	fdist = nltk.FreqDist(collection)
	bigrams = nltk.bigrams(collection)
	fdist_bigrams = nltk.FreqDist(bigrams)
	for word in word_list:
		if " " in word:
			bigram = tuple(word.split())
			print word, ":", fdist_bigrams[bigram] / len(collection)
		else:
			print word, ":", fdist[word] / len(collection)

def average_letters_per_word(collection):
	numWords = len(collection)
	word_lengths = []
	for word in collection:
		word_lengths.append(len(word))

	return sum(word_lengths) / numWords

def main():
	current_directory = os.path.dirname(__file__)
	corpus_root = os.path.abspath(current_directory)
	wordlists = PlaintextCorpusReader(corpus_root, 'Islip13Rain/.*\.txt')
	wordlists.fileids()
	ClassEvent = nltk.Text(wordlists.words())
	CEWords = ["Long Island", "Weather Service", "flooding", "August", 
		"heavy rains", "Wednesday", "Suffolk County", "New York", "rainfall",
		"record"]

	# ClassEvent Statistics
	print "--------- CLASS EVENT STATISTICS -------------"
	print "ClassEvent non stopwords", non_stopword_fraction(ClassEvent)	
	print "ClassEvent WORD LENGTH DISTRIBUTIONS:"
	print_word_length_distributions(ClassEvent)
	print "ClassEvent PERCENTAGE OF WORD OCCURRENCES:"
	print_percentage_of_word_in_collection(ClassEvent, CEWords)
	
	ClassEventLettersPerWord = average_letters_per_word(ClassEvent)
	ClassEventWordsPerSent = len(wordlists.words()) / len(wordlists.sents())
	ClassEventARI = (4.71 * ClassEventLettersPerWord) + (0.5 * \
		ClassEventWordsPerSent) - 21.43
	
	print "Average number of letters per word", ClassEventLettersPerWord
	print "Average number of words per sentence:", ClassEventWordsPerSent
	print "Automated Readability Index:", ClassEventARI


	print 

	wordlists_event = PlaintextCorpusReader(corpus_root, "Texas_Wild_Fire/.*\.txt")
	wordlists_event.fileids()
	YourSmall = nltk.Text(wordlists_event.words())
	SmallEventWords = ["Fire", "Wildfire", "Water", "Damage", "Ground", "Burn", 
		"Town", "Heat", "Wind", "Speed", "Size", "City", "People", "Home",
		"Weather", "Debris", "Death", "Smoke", "State", "Ash"]
	

	# YourSmall statistics
	print "--------- YOUR SMALL STATISTICS --------------"
	print "Texas_Wild_Fire", non_stopword_fraction(YourSmall)
	print "YourSmall WORD LENGTH DISTRIBUTIONS:"
	print_word_length_distributions(YourSmall)
	print "YourSmall PERCENTAGE OF WORD OCCURRENCES:"
	print_percentage_of_word_in_collection(YourSmall, SmallEventWords)
	
	YourSmallLettersPerWord = average_letters_per_word(YourSmall)
	YourSmallWordsPerSent = len(wordlists_event.words()) / \
		len(wordlists_event.sents())
	YourSmallARI = (4.71 * YourSmallLettersPerWord) + (0.5 * \
		YourSmallWordsPerSent) - 21.43

	print "Average number of letters per word", YourSmallLettersPerWord
	print "Average number of words per sentence:", YourSmallWordsPerSent
	print "Automated Readability Index", YourSmallARI

if __name__ == "__main__": main()