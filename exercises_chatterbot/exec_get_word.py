import nltk
import re
import requests
import urllib.request
from bs4 import BeautifulSoup
import collections

nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('portuguese')

ativo = input("Digite a palavra: ")

print('Vou analisar meu texto sobre '+ativo)

response = urllib.request.urlopen('https://pt.wikipedia.org/wiki/'+ativo)
# response = requests.get('https://statusinvest.com.br/acoes/'+ativo)

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

def palavra_mais_frequente(arr):
    contador = collections.Counter(arr)
    return contador.most_common(1)[0][0]

# palavra_mais_frequente(freq_words)

print('A palavra mais frequente é: ', palavra_mais_frequente(freq_words))
# for index, value in freq_words.items():
#     if index == 'erechim':
#         print('Word[' + str(index) + ']: ' + str(value))

# freq_words.plot(5)