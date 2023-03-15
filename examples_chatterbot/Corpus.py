from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Criamos um novo Chatbot chamado MaladaBot
chatbot = ChatBot('MadalaBot')

# Criamos um "treinador" que será baseado em um "corpus"
trainer = ChatterBotCorpusTrainer(chatbot)
# Define o corpus para portugues
trainer.train('chatterbot.corpus.portuguese')

# Exporta o arquivo com conteudo treinado
trainer.export_for_training('./data.json')