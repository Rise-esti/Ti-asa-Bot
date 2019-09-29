import chatterbot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


chatbot = ChatBot(
    "@ti-asa",
    database_uri='sqlite:///db/ti-asa.db',
    logic_adapters=[
        {
            'import_path': "chatterbot.logic.BestMatch",
            'default_response': 'Je ne comprends ce que vous dites',
            'maximum_similarity_threshold':  0.90
        },

        {
            'import_path': "chatterbot.logic.MathematicalEvaluation",
            'language': chatterbot.languages.FR
         }
    ],
)

trainer = ListTrainer(chatbot)

while True:
    enter = input('>> ')
    if enter == 'quit':
        break
    ques = chatbot.get_response(enter)
    print(ques)

print('Bye!')
