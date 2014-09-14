__author__ = 'Souleiman Ayoub'
__date__ = '9/1/2014'
# Python routine submitted to aid work on VT CS4984, Computational Linguistics

import nltk
from nltk.corpus import stopwords


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
