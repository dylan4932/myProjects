from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chatbot
bot = ChatBot('MyBot')

# Define some training data
training_data = [
    'Hello',
    'Hi there!',
    'How are you?',
    'I am doing well.',
    'That is good to hear.',
    'Thank you',
    'You are welcome.'
]

# Train the chatbot
trainer = ListTrainer(bot)
trainer.train(training_data)

# Start a conversation with the chatbot
while True:
    try:
        user_input = input('You: ')
        bot_response = bot.get_response(user_input)
        print('Bot: ', bot_response)

    # Exit the program if the user types 'quit'
    except KeyboardInterrupt:
        break
