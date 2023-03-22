import nltk
import re
import requests
import urllib.request
from bs4 import BeautifulSoup
import collections
import tweepy

nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('portuguese')

nick = input("Digite o usuário: ")

print('Buscando tweets do user '+nick)

response = urllib.request.urlopen('https://pt.wikipedia.org/wiki/'+nick)

html = response.read()
webscrap = BeautifulSoup(html, 'html5lib')

content = webscrap.get_text(strip=True)
content = content.lower()

content = re.sub(r'[^\w\s]', ' ', content)
content = re.sub("\d+", ' ', content)

text_words = [t for t in content.split()]

acceptable_words = []

for word in text_words:
    if word not in stopwords and len(word) < 30 and len(word) > 3:
        acceptable_words.append(word)

freq_words = nltk.FreqDist(acceptable_words)

def frequent_word(arr):
    count = collections.Counter(arr)
    return count.most_common(1)[0][0]

# palavra_mais_frequente(freq_words)

print('A palavra mais frequente é: ', frequent_word(freq_words))
# for index, value in freq_words.items():
#     if index == 'erechim':
#         print('Word[' + str(index) + ']: ' + str(value))

# freq_words.plot(5)