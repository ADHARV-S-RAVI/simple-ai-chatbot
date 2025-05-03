import random

# Predefined responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey! How can I help?"],
    "how are you": ["I'm just code, but I'm doing great!", "All systems operational!"],
    "what is your name": ["I'm a chatbot made by Adharv!", "You can call me SCK-Bot."],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "help": ["I can answer basic questions like your name, greeting, or status."]
}

# Function to get response
def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return "Sorry, I don't understand that. Try asking something else."

# Chat loop
print("SCK-Bot: Hello! Ask me anything. Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if "bye" in user_input.lower():
        print("SCK-Bot:", random.choice(responses["bye"]))
        break
    response = get_response(user_input)
    print("SCK-Bot:", response)
