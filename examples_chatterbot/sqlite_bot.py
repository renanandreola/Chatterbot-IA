from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Criamos um novo Chatbot chamado MaladaBot
chatbot = ChatBot('MadalaBot', 
    logic_adapters=[
        "chatterbot.logic.MathematicalEvaluation",
        "chatterbot.logic.TimeLogicAdapter"
    ],
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite0')

# Laço de repetição para a conversa acontecer
while True:
    #Solicita uma entrada de dados para o usuário
    pergunta = input("Usuário: ")
    # Busca resposta do MadalaBot
    resposta = chatbot.get_response(pergunta)
    
     # Se o grau de confiança do chatbot for inferior a 0.5, informa que não sabe o que responder
    if float(resposta.confidence) > 0.5:
        print('MadalaBot: ', resposta)
    else:
        print('MadalaBot: Me desculpe! Não tenho uma resposta para essa pergunta.')