from __future__ import division
import os, nltk, pickle

dir_path = os.path.dirname(__file__)
# feature_list_file_name = 'SmallFeatures.txt'
feature_list_file_name = 'LargeFeatures.txt'

file = os.path.join(dir_path, feature_list_file_name)

#yoursmallwords = os.path.join(dir_path, 'YourSmallWords.txt')

feature_list = []

with open(file, 'r') as f:
    for line in f.readlines():
    	# Only care about word
  	# count, word, tag = line.split('\t')	
  	word = line.strip()
	word = word.lower()
        if (word.isalpha()):
	    feature_list.append(word)

''' Only needed for the Small Feature Set    
with open(yoursmallwords, 'r') as f:
    for line in f.readlines():
	line = line.strip()
        feature_list.append(line)
'''

feature_list = set(feature_list)

#pickle_name = 'SmallFeatures.pickle'
pickle_name = 'LargeFeatures.pickle'
pickle_obj = open(pickle_name, 'wb')
pickle.dump(feature_list, pickle_obj)
pickle_obj.close()

pickle_obj = open(pickle_name, 'r')
p = pickle.load(pickle_obj)
pickle_obj.close()
print p
print ("fire" in p)

for file in p:
    print file
