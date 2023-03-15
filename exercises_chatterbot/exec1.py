# 1 - Informar	o	criador	e	o	ano	de	criação	de	uma	linguagem	de	programação	informada	pelo	usuário(ao	menos	10	linguagens)

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Criamos um novo Chatbot chamado MaladaBot
chatbot = ChatBot('MadalaBot')

# Criamos um "treinador" para o MadalaBot
trainer = ListTrainer(chatbot)

conversa = ['C', 'Criada em 1972',
            'Javascript', 'Criada em 1995',
            'C#', 'Criada em 1999',
            'Java', 'Criada em 1991',
            'Dart', 'Criada em 2011',
            'Kotlin', 'Criada em 2011'
            'Python', 'Criada em 1991'
            'C++', 'Criada em 1980'
            'Go', 'Criada em 2009'
            'Swift', 'Criada em 2014'
            ]

# Executamos o treinamento do MadalaBot com conjunto de palavras/sentenças
trainer.train(conversa)

# Laço de repetição para a conversa acontecer
while True:
    #Solicita uma entrada de dados para o usuário
    pergunta = input("Digite o nome da linguagem: ")
    resposta = chatbot.get_response(pergunta)

    # Se o grau de confiança do chatbot for inferior a 0.5, informa que não sabe o que responder
    if float(resposta.confidence) > 0.5:
        print('MadalaBot: ', resposta)
    else:
        print('MadalaBot: Me desculpe! Não tenho uma resposta para essa pergunta.')