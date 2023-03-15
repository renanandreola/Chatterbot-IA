# 2 - Informar	a	capital	de	um	país	informado	pelo	usuário(ao	menos	15	países)

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Criamos um novo Chatbot chamado MaladaBot
chatbot = ChatBot('MadalaBot')

# Criamos um "treinador" para o MadalaBot
trainer = ListTrainer(chatbot)

conversa = ['Afeganistão', 'A capital é Cabul',
            'África do Sul', 'A capital é Pretória',
            'Bahamas', 'A capital é Nassau',
            'Brasil', 'A capital é Brasília',
            'Bélgica', 'A capital é Bruxelas',
            'Bulgária', 'A capital é Sófia'
            'Cabo Verde', 'A capital é Praia'
            'Camboja', 'A capital é Pnom Pene'
            'Canadá', 'A capital é Otava'
            'Catar', 'A capital é Doa'
            'Cazaquistão', 'A capital é Astana'
            'Chile', 'A capital é Santiago'
            'China', 'A capital é Pequim'
            'Colômbia', 'A capital é Bogotá'
            'Costa Rica', 'A capital é São José'
            ]

# Executamos o treinamento do MadalaBot com conjunto de palavras/sentenças
trainer.train(conversa)

# Laço de repetição para a conversa acontecer
while True:
    #Solicita uma entrada de dados para o usuário
    pergunta = input("Digite o nome do país: ")
    resposta = chatbot.get_response(pergunta)

    # Se o grau de confiança do chatbot for inferior a 0.5, informa que não sabe o que responder
    if float(resposta.confidence) > 0.5:
        print('MadalaBot: ', resposta)
    else:
        print('MadalaBot: Me desculpe! Não tenho uma resposta para essa pergunta.')