#!/usr/bin/python3

from flask import Flask, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


chatbot = ChatBot(
    "@ti-asa",
    database_uri='sqlite:////home/esti/Ti-asa-Bot/db/ti-asa.db',
    logic_adapters=[
        "chatterbot.logic.BestMatch"
    ],
)

trainer = ListTrainer(chatbot)

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def listen():
    text = request.form.get('text')
    print(text)
    text = chatbot.get_response(text.strip()[1:-1])
    print(text)
    return str(text)

    #  return str(chatbot.get_response(request.form.get('text')))


if __name__ == '__main__':
    app.run()
