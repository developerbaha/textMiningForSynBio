import urllib.request
import string
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

words = text_tokens.split()
# remove punctuation from each word


table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in words]
words = [word for word in text_tokens if word.isalpha()]

for words in text_tokens:
    fdist[words.lower()] += 1
fdist1 = fdist.most_common(100)
print(fdist1)
