from __future__ import division
import os, nltk, pickle

dir_path = os.path.dirname(__file__)
file = os.path.join(dir_path, 'SmallFeatures.txt')
yoursmallwords = os.path.join(dir_path, 'YourSmallWords.txt')

feature_list = []

with open(file, 'r') as f:
    for line in f.readlines():
    	# Only care about word
  	# count, word, tag = line.split('\t')	
  	word = line.strip()
	word = word.lower()
        if (word.isalpha()):
	    feature_list.append(word)
    
with open(yoursmallwords, 'r') as f:
    for line in f.readlines():
	line = line.strip()
        feature_list.append(line)

feature_list = set(feature_list)

pickle_name = 'SmallFeatures.pickle'
pickle_obj = open(pickle_name, 'wb')
pickle.dump(feature_list, pickle_obj)
pickle_obj.close()

pickle_obj = open(pickle_name, 'r')
p = pickle.load(pickle_obj)
pickle_obj.close()
print p
print ("fire" in p)
