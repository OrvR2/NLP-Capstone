#!/usr/bin/env python
import sys, zipimport

importer = zipimport.zipimporter('nltk.mod')
nltk = importer.load_module('nltk')

nltk.data.path += ["./nltkData/"]
# YourWords Array
YourWords = ["long island", "weather service", "flooding", "august", 
    "heavy rains", "wednesday", "suffolk county", "new york", "rainfall",
    "record"]

YourWords = set(YourWords)

# input comes from STDIN (standard input)
for line in sys.stdin:
  # remove leading and trailing whitespace
  line = line.strip()
  # split the line into words
  textwords = line.split()
  #textpairs = [line[i] + ' ' + line[i + 1] for i in range(len(line) - 1)]

  #stopwords_list = stopwords.words('english')
  '''for w in textwords:
    w = w.lower()
    if w in YourWords:
      print '%s\t%s' % (w, 1)
    else:
      print 'other\t%s' % (1)'''

  for i in range(0, len(textwords) - 1):
    w1 = textwords[i]
    w2 = textwords[i + 1]
    w = w1 + " " + w2
    if w in YourWords:
      print "%s\t%s" % (w, 1)
    else:
      print "other\t%s" % (1)