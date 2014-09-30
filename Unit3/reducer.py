import sys
import nltk
from operator import itemgetter
from nltk.corpus import stopwords

stopwords_list = stopwords.words('english')
word = None
tag = None
current_word = None
curent_tag = None
current_count = 0

for line in sys.stdin:

    line = line.strip() # remove whitespace

    count, word, tag = line.split(',', 2) # splits tuple into 3 parts
    word = word.lower()
    
    if word not in stopwords_list:
        if current_word == word and current_tag == tag:
            current_count += count
        else:
            if current_word and current_tag:
                print '{}\t{}\t{}'.format(current_count, current_word, current_tag)
            current_word = word
            current_tag = tag
            current_count = count
   
if current_word == word:
    print '{}\t{}\t{}'.format(current_count, current_word, current_tag)
