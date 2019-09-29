from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Gaetan Jonathan",
                   logic_adapters=[
        "chatterbot.logic.BestMatch"
    ])

# exemple de donnée d'entrainement
conversation = ["Salut", "@ti-asa Bot vous Salut", "ça va?", "oui et toi",
                "ça va aussi", "cool"]

trainer = ListTrainer(chatbot)

trainer.train(conversation)

while True:
    enter = input('>> ')
    if enter == 'quit':
        break
    ques = chatbot.get_response(enter)
    print(ques)
