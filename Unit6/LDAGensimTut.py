'''
#Topic identification using LDA (gensim) example-Code:
#Created on Oct 15, 2014
#Authors: Xuan Zhang and Tarek Kanan
'''

from gensim import corpora, models
from nltk.corpus import stopwords
from nltk.corpus import PlaintextCorpusReader

#Call the NLTK stop words list
stoplist = stopwords.words('english')

customStops = ['-', '|', '(1)', '&']

print 'creating small reader'
corpus_root = '../large_articles'
yourSmallReader = PlaintextCorpusReader(corpus_root, '.*')

#Remove the stop words
print 'removing stop words'
texts = [[word for word in yourSmallReader.raw(fileid).lower().split() if word not in stoplist and word not in customStops] for fileid in yourSmallReader.fileids()]

#Build the dictionary and the corpus
print 'build dictionary'
dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]

#Define the LDA model and the number of topics.
print 'define lda'
notopics = 50
lda = models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=notopics)

#Printing the topic with their probabilities
print "\n\n", notopics, "Topics with their corresponding probabilities\n"
for i in range(0, lda.num_topics):
    print "Topic", i+1, ":", lda.print_topic(i)
