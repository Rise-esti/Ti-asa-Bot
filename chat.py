from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


chatbot = ChatBot(
    "@ti-asa",
    database_uri='sqlite:///db/ti-asa.db',
    logic_adapters=["chatterbot.logic.BestMatch"],
)

trainer = ListTrainer(chatbot)

while True:
    enter = input('>> ')
    if enter == 'quit':
        break
    ques = chatbot.get_response(enter)
    print(ques)

print('Bye!')
