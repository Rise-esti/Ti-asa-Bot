from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import pickle

chatbot = ChatBot(
    "@ti-asa",
    database_uri='sqlite:///db/ti-asa.db',
    logic_adapters=["chatterbot.logic.BestMatch"],
)

# exemple de donnée d'entrainement
conversation = [
    "Bonjour", "Bonjour!"
    "Besoin de travail", "ça tombe bien, ti-asa est là pour vous aider",
    "Comment allez-vous", "Super en forme"
]


trainer = ListTrainer(chatbot)
# trainer.train('./salfr.json')

res = os.popen('ls dataset')
res = res.read().split('\n')

try:
    res.remove('')
except:
    pass
i = 0
for file in res:
    try:
        with open('dataset/' + file, 'rb') as trainSet:
            ds = pickle.load(trainSet)
        trainer.train(ds)
        print(f" {i} fichier d'entrainement trouvé(s)...")
        i += 1
    except:
        pass
while True:
    enter = input('>> ')
    if enter == 'quit':
        break
    ques = chatbot.get_response(enter)
    print(ques)
