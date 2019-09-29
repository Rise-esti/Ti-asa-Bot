from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot(
    "@ti-asa",
    logic_adapters=["chatterbot.logic.BestMatch"],
)

# exemple de donnée d'entrainement
conversation = [
    "Bonjour", "Bonjour!"
    "Besoin de travail", "ça tombe bien, ti-asa est là pour vous aider",
    "Comment allez-vous", "Super en forme"
]
trainer = ListTrainer(chatbot)
trainer.train('./salfr.json')

while True:
    enter = input('>> ')
    if enter == 'quit':
        break
    ques = chatbot.get_response(enter)
    print(ques)
