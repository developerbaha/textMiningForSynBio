import urllib.request
import re
import requests as requests
from bs4 import BeautifulSoup
import nltk
import urllib
import urlopen
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize

# providing url
fdist = FreqDist()
response = requests.get('https://parts.igem.org/Part:BBa_R0040').content
soup = BeautifulSoup(response, "html.parser")
text_tokens = nltk.tokenize.word_tokenize(soup.get_text())
punctuation = re.compile(r"[.?!,:;()|0-9]")
post_punctuation = []
for word in text_tokens:
    word = punctuation.sub("", word)
    if len(word) > 0:
        post_punctuation.append(word)
for word in post_punctuation:
    fdist[word.lower()] += 1
    fdist1 = fdist.most_common(50)
print(fdist1)
