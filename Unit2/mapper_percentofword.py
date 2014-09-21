#!/usr/bin/env python
import sys, zipimport

importer = zipimport.zipimporter('nltk.mod')
nltk = importer.load_module('nltk')

nltk.data.path += ["./nltkData/"]
#from nltk.corpus import stopwords

# input comes from STDIN (standard input)
for line in sys.stdin:
  # remove leading and trailing whitespace
  line = line.strip()
  # split the line into words
  textwords = line.split()
  
  #stopwords_list = stopwords.words('english')
  for w in textwords:
    w = w.lower()
    length = len(w)
    if length <= 15:
      print '{}\t{}'.format(length, 1)
    else: 
      print 'other\t{}'.format(1)
    