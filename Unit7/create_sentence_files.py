import nltk
from nltk.corpus import PlaintextCorpusReader
import pickle
import os
from time import gmtime, strftime

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

keywordsList = 'contained,devastating,stopped,destruction,blaze,smoldering,victims,flames,closed,deaths,residents,fire,damage,burn,heat,size,weather,smoke,houses,neighborhood,battling,acre,homes,shelter,square,wind,town,wildfire'.split(',')
english = pickle.load(open('../nltk_data/tokenizers/punkt/english.pickle', 'r'))

corpus_root = './Large_Articles'
reader = PlaintextCorpusReader(corpus_root, '.*', sent_tokenizer=english)

sents = reader.sents()

folder_name = 'results_' + strftime("%Y-%m-%d %H:%M:%S", gmtime())
os.mkdir(folder_name)

# Loop through each file
for fileid in reader.fileids():

    # Get sentences from each file
    sents = reader.sents(fileid)
    for i, sent in enumerate(sents):

        # Remove sentences under 3 words
        if any(keyword in sent for keyword in keywordsList) and len(sent) > 3:
            f = open(folder_name + '/' + fileid.replace('.txt','') + '-' + str(i) + '.txt', 'w')
            for word in sent:
            	if not is_ascii(word):
            		break
            else:
            	f.write(' '.join(sent))
	        f.close()

print 'done'
