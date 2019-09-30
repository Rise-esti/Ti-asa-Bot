from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

enter = ''


def command(value):
    return "Hello World" + value


chatbot = ChatBot(
    "@ti-asa",
    database_uri='sqlite:///db/ti-asa.db',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',
            'input_text': 'tiasa',
            'output_text': command(enter)
        },
        {
            'import_path': "chatterbot.logic.BestMatch",
            'maximum_similarity_threshold':  0.20
        },

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
