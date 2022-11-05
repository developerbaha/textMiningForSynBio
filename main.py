import urllib.request
import re
import requests as requests
from bs4 import BeautifulSoup
import nltk
import urllib
import urlopen
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
from nltk.util import bigrams, trigrams, ngrams

# providing url
fdist = FreqDist()
all_stopwords = stopwords.words('english')
list_stopwords = ['the', 'part', 'page', 'iptg', 'MM', 'IPTG', 'Part', 'The', 'mM', '-', 'R', 'There']
all_stopwords.extend(list_stopwords)

base_url = ('https://parts.igem.org/Part:BBa_R00')
page_number = 10
while page_number != 200:
    url = base_url + str(page_number)
    response = requests.get(url).text
    soup = BeautifulSoup(response, "html.parser")
    page_number = page_number + 1
    punctuation = re.compile(r'[.?!,:;()|%]')
    post_punctuation = []
    text_tokens = nltk.tokenize.word_tokenize(soup.get_text())
    tokens_without_sw = [word for word in text_tokens if not word in all_stopwords]
    for word in tokens_without_sw:
        word = punctuation.sub("", word)
        if len(word) > 0:
            post_punctuation.append(word)
    for word in post_punctuation:
        fdist[word.lower()] += 1
        fdist1 = fdist.most_common(50)
print(fdist1)
