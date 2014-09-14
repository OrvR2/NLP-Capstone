import nltk
from nltk.corpus import PlaintextCorpusReader
import os
import collocation

def collocation(text, limit=20):
    best_pair_table = {}

    filter = lambda word: word in stopwords.words('english') or not word.isalpha()

    for tup in nltk.bigrams(text):
        if filter(tup[0]) or filter(tup[1]):
            continue

        count = best_pair_table.get(tup)
        best_pair_table[tup] = 1 if not tup in best_pair_table else count + 1

    return sorted([(count, key) for key, count in best_pair_table.items()],
                  key=lambda t: t[0], reverse=True)[:limit]

current_directory = os.path.dirname(__file__)
corpus_root = os.path.abspath(current_directory)

wordlists = PlaintextCorpusReader(corpus_root, "Texas_Wild_Fire/.\.txt")
YourSmall = nltk.Text(wordlists.words())

# Used for frequency distribution information.
#YourSmallFreqDist = FreqDist(YourSmall)
#YourSmallSet = set(YourSmall)

# optional function parameter for number of collocations. default 20.
YourSmallCollocations = collocation.collocation(YourSmall)
print YourSmallCollocations