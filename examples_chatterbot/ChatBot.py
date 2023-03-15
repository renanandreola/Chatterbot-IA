from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Criamos um novo Chatbot chamado MaladaBot
chatbot = ChatBot('MadalaBot')

# Criamos um "treinador" para o MadalaBot
trainer = ListTrainer(chatbot)

conversa = ['Oi' , 'Olá, Tudo bem?',
            'Mama aqui', 'Sai dai gayzão',
            'Lise', 'Comi no cuspe',
            'Tudo bem?', 'Tudo ótimo',
            'Você gosta de programar?', 'Sim, eu programo em Python',
            'Você torce para quem?', 'Somos tricolor, perdemos a coopaa... Gremista, mesmo assim!'
            ]

# Executamos o treinamento do MadalaBot com conjunto de palavras/sentenças
trainer.train(conversa)

# Laço de repetição para a conversa acontecer
while True:
    #Solicita uma entrada de dados para o usuário
    pergunta = input("Usuário: ")
    resposta = chatbot.get_response(pergunta)

    # Se o grau de confiança do chatbot for inferior a 0.5, informa que não sabe o que responder
    if float(resposta.confidence) > 0.5:
        print('MadalaBot: ', resposta)
    else:
        print('MadalaBot: Me desculpe! Não tenho uma resposta para essa pergunta.')