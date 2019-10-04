#coding : utf-8

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import pickle
import sqlite3
from datetime import datetime

bdd = sqlite3.connect('db/trainingSet.db')
sql = bdd.cursor()

chatbot = ChatBot(
    "@ti-asa",
    database_uri='sqlite:///db/ti-asa.db',
)

trainer = ListTrainer(chatbot)

res = os.popen('ls dataset')
res = res.read().split('\n')

try:
    res.remove('')

except ValueError:
    pass

i = 1

for fic in res:
    try:
        sql.execute("INSERT INTO TrainSET VALUES (?)", (fic,))

        with open('dataset/' + fic, 'rb') as trainSet:
            ds = pickle.load(trainSet)
        trainer.train(ds)

        print(f" {i} nouveau fichier d'entrainement trouvé(s)...")
        os.popen(f"echo '{datetime.today()}: {fic} nouveau fichier d'entrainement trouvé(s)...'>>train.log")

        i += 1

    except sqlite3.IntegrityError:
        os.popen(f"echo '{datetime.today()}: {fic} deja entrainer'>>train.log")

    else:
        bdd.commit()
bdd.close()
