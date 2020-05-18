from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Charlie')
trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(
    "chatterbot.corpus.korean"
)

while True:
    try:
        user_input = input()

        bot_response = chatbot.get_response(user_input)

        print(bot_response)
    
    except (KeyboardInterrupt, EOFError, SystemExit):
        break