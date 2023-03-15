# 3 - Pense	na	ideia	de	um	produto,	utilizando	adaptadores	lógicos,	e	desenvolva	alguma	solução(não	precisa	ser	uma	solução	completa,	pode	ser	algo	parcial)

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from pymongo import MongoClient

# Criamos um novo Chatbot chamado MaladaBot
chatbot = ChatBot('MadalaBot')

# Criamos um "treinador" para o MadalaBot
trainer = ListTrainer(chatbot)

def get_database():
 
   # Mongodb atlas url
   CONNECTION_STRING = "mongodb+srv://renan:renan@contatosmobile-pjbzy.gcp.mongodb.net/receitas?retryWrites=true&w=majority"
 
   # Cria a conexão mongo client
   client = MongoClient(CONNECTION_STRING)
 
   # Cria a base de dados
   return client['DatabaseReceitas']
  
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":   
  
   # Pega a base de dados
   dbname = get_database()

dbname = get_database()
collection_name = dbname["receitas"]

item_1 = {
  "name" : "Sanduíche",
  "desc" : "A sugestão dessa receita é cobrir o pão com linguiça portuguesa ou calabresa. Além disso, outros itens também entram em cena para deixar sua refeição ainda mais gostosa, como o purê de tomate, o pepino e vários temperos. A lista de ingredientes não é das mais curtas, mas o sabor é tão gostoso, que vale a pena testar."
}

item_2 = {
  "name" : "Pudim",
  "desc" : "Em uma panela em fogo médio derreta o açúcar até atingir o ponto de caramelo. Adicione o caramelo em uma forma de 18cm e deixe esfriar. Em uma tigela misture o leite condensado, o leite e os ovos e misture até que fique bem homogêneo. Adicione a mistura na forma com a calda e cubra com papel alumínio, leve para a Air Fryer + Forno Mondial dentro de uma forma com 2 dedos de água em banho maria por uma hora a 180ºC"
}

item_3 = {
  "name" : "Macarrão",
  "desc" : "Comece colocando o macarrão na Panela de Pressão Elétrica Mondial, juntamente com todos os demais ingredientes. Misture todos os ingredientes, tampe a panela, coloque a válvula na posição de pressão e programe por 10 minutos em qualquer função de cozimento. Quando o tempo terminar, retire a pressão, abra a panela, misture bem até ficar homogêneo e já pode servir. Se quiser pode adicionar 2 ou 4 tipos de queijos diferentes para ter um macarrão aos 2 ou 4 queijos, fica incrível!"
}

# Cadastra informações na base
collection_name.insert_many([item_1,item_2,item_3])
  
conversa = []

item_details = collection_name.find()
for item in item_details:
   # Popula a conversa
   print(item)
   conversa.append(item['name'])
   conversa.append(item['desc'])

# Executamos o treinamento do MadalaBot com conjunto de palavras/sentenças
trainer.train(conversa)

# Laço de repetição para a conversa acontecer
while True:
    #Solicita uma entrada de dados para o usuário
    pergunta = input("Digite o nome da receita: ")
    resposta = chatbot.get_response(pergunta)

    # Se o grau de confiança do chatbot for inferior a 0.5, informa que não sabe o que responder
    if float(resposta.confidence) > 0.5:
        print('MadalaBot: ', resposta)
    else:
        print('MadalaBot: Me desculpe! Não tenho uma resposta para essa pergunta.')