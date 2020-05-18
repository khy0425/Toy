from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


conversation = [
    "Hello",
    "Hi there!",
    "How are you doing",
    "I`m doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome.",
    "Hi, can I help you?",
    "Sure, I'd like to book a flight to Iceland.",
     "Your flight has been booked."
]

chatbot = ChatBot('Charlie')

trainer = ListTrainer(chatbot)

trainer.train(conversation)

response = chatbot.get_response("Good morning!")
print(response)

response = chatbot.get_response('I would like to book a flight.')
print(response)