#!/usr/bin/env python

import sys, zipimport
# from operator import itemgetter

reload(sys)
sys.setdefaultencoding('utf-8')

importer = zipimport.zipimporter('nltk.mod')
nltk = importer.load_module('nltk')
nltk.data.path += ["./nltkData/"]

stopwords_list = nltk.corpus.stopwords.words('english')
word = None
tag = None
current_word = None
curent_tag = None
current_count = 0

listOfBigrams = []
Bigram = []
p = re.compile('\(\'[a-z]+\'\,\s*\'[a-z]+\'\)')
# create list of bigrams
for line in open('Bigrams10k.txt'):
    Bigram = p.findall(line)
    listOfBigrams.append(Bigram)


for line in sys.stdin:

    line = line.strip() # remove whitespace

    word, word2, tag, count = line.split(',', 3) # splits tuple into 4 parts, where word = middle word and word2 is
                                                 # the word before or after in the bigram

    try:
        count = int(count)
    except ValueError:
        continue

    bigram = [word, word2]
    if bigram in listOfBigrams:
        if current_bigram == bigram:
            current_count += count
        else:
            if current_bigram:
                print '{2}\t{0}'.format(current_bigram, current_count)
            current_bigram = bigram
            current_count = count

if current_bigram == bigram:
    print '{2}\t{0}'.format(current_bigram, current_count)

