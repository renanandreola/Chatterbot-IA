import nltk
import re
import requests
import urllib.request
from bs4 import BeautifulSoup
import collections
import tweepy
from pymongo import MongoClient

nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('portuguese')

nick = input("Digite o usuário: ")

print('Buscando tweets do user '+ nick)

# CADASTRO NO BANCO

def get_database():
   CONNECTION_STRING = "mongodb+srv://admin:admin@iacluster.hg5m0vb.mongodb.net/?retryWrites=true&w=majority"
 
   # Cria a conexão mongo client
   client = MongoClient(CONNECTION_STRING)
 
   # Cria a base de dados
   return client['DatabaseTwitter']
  
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":   
  
   # Pega a base de dados
   dbname = get_database()

dbname = get_database()

collection_name = dbname["tweets"]
collection_name_words = dbname["words"]

tweet_1 = {
  "username" : "renan",
  "tweet" : "Hoje tive uma aula muito foda"
}

tweet_2 = {
  "username" : "renan",
  "tweet" : "Que foda isso mano"
}

tweet_3 = {
  "username" : "renan",
  "tweet" : "Porque o python é tão foda ?"
}

# Cadastra informações na base
collection_name.insert_many([tweet_1,tweet_2,tweet_3])

# FIM CADASTRO NO BANCO

# PEGA DADOS DO BANCO
tweets = collection_name.find()

html = ""
user_TW = ""

for tweet in tweets:
#    print(tweet['tweet'])
   html += tweet['tweet']
   user_TW = tweet['username']
   
# FIM PEGA DADOS DO BANCO

# response = urllib.request.urlopen('https://pt.wikipedia.org/wiki/'+nick)
# html = response.read()

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

# Verifica palavra mais frequente
def frequent_word(arr):
    count = collections.Counter(arr)
    return count.most_common(1)[0][0]

word_send = frequent_word(freq_words)
print('A palavra mais frequente é: ', word_send)

# Adiciona user e palavra mais frequente no banco
words = {
  "username" : user_TW,
  "word" : word_send
}
collection_name_words.insert_many([words])

# for index, value in freq_words.items():
#     if index == 'erechim':
#         print('Word[' + str(index) + ']: ' + str(value))

freq_words.plot(5)