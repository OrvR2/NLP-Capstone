import os, sys, pickle, zipimport
from time import gmtime, strftime

importer = zipimport.zipimporter('../nltk.mod')
nltk = importer.load_module('nltk')

corpus_root = '../Large_Relevant'

folder_name = 'results_' + strftime("%Y-%m-%d %H:%M:%S", gmtime())
os.mkdir(folder_name)
sent_tokenizer = nltk.data.load('../Zips/nltk_data/tokenizers/punkt/english.pickle')
keywordsList = pickle.load(open('../LargeFeatures.pickle', 'rb'))

# Loop through each file
for fileid in os.listdir(corpus_root):

    f = os.path.join(corpus_root, fileid)
    f = open(f, 'r')
    fwords = f.read().decode('utf8', 'ignore')
    f.close()
    # Get sentences from each file
    sents = sent_tokenizer.tokenize(fwords)
    for i, sent in enumerate(sents):

        # Remove sentences under 3 words
        if any(keyword in sent for keyword in keywordsList) and len(sent) > 3:
            f = open(folder_name + '/' + fileid.replace('.txt','') + '-' + str(i) + '.txt', 'w')
            f.write(' '.join(sent).encode('utf8', 'ignore'))
            f.close()

print 'done'
