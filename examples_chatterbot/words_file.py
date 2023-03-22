import nltk
import re
import urllib.request
from bs4 import BeautifulSoup

nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('portuguese')

# response = urllib.request.urlopen('https://pt.wikipedia.org/wiki/Erechim')
# html = response.read()
# webscrap = BeautifulSoup(html, 'html5lib')

# content = webscrap.get_text(strip=True)
# content = content.lower()

arq = open('text.txt', 'r+')
content = arq.read()
content = content.lower()

content = re.sub(r'[^\w\s]', ' ', content)
content = re.sub("\d+", ' ', content)

text_words = [t for t in content.split()]

acceptable_words = []

for word in text_words:
    if word not in stopwords and len(word) < 30 and len(word) > 3:
        acceptable_words.append(word)

freq_words = nltk.FreqDist(acceptable_words)

for index, value in freq_words.items():
    if index == 'erechim':
        print('Word[' + str(index) + ']: ' + str(value))

freq_words.plot(5)