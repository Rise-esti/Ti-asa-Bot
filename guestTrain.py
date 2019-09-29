import pickle
import time

print("Bienvenue cher Contributeur")

print("Vous allez lancer une discussion entre un individu A et B")

print("Pour terminer une conversation, Ecriver: `quit` ")

titre = input("Entrer le titre de la discussion: ")

autor = input("Entrer votre prenom (contributeur): ")

print("\nDemarage.. \n\n")

discuss = []
while True:
    text = input('[A] >> ')
    if text == 'quit':
        break
    discuss.append(text)
    text = input('[B] >> ')
    if text == 'quit':
        break
    discuss.append(text)


fileName = './dataset/' + autor + str(time.time()) + '.pickle'

with open(fileName, 'wb') as file:
    pickle.dump(discuss, file)
