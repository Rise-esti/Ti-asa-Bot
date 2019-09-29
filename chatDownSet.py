from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot(
    "@ti-asa",
    database_uri='sqlite://db/db.sqlite3',
    logic_adapters=["chatterbot.logic.BestMatch"],
)

trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train('chatterbot.corpus.french.greetings')

trainer.export_for_training('./salfr.json')
