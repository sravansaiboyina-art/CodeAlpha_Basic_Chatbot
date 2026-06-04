def show_welcome_message():
    print("===================================")
    print("      SIMPLE PYTHON CHATBOT")
    print("===================================")
    print("Chatbot : Hello! I am your assistant.")
    print("Chatbot : Type 'bye' to exit the chat.")
    print("===================================")
def get_bot_response(user_message):
    message = user_message.lower()
    if message == "hello":
        return "Hi! Nice to meet you."

    elif message == "hi":
        return "Hello! How can I help you?"

    elif message == "how are you":
        return "I'm fine, thanks for asking!"

    elif message == "what is your name":
        return "My name is Python Chatbot."

    elif message == "what is python":
        return "Python is a popular programming language."

    elif message == "good morning":
        return "Good Morning! Have a great day."

    elif message == "good evening":
        return "Good Evening!"

    elif message == "thank you":
        return "You're welcome!"

    elif message == "bye":
        return "Goodbye! See you again."

    else:
        return "Sorry, I don't understand that."

def start_chatbot():

    show_welcome_message()

    while True:

        user_input = input("You : ")

        bot_reply = get_bot_response(user_input)

        print("Chatbot :", bot_reply)

        if user_input.lower() == "bye":
            print("===================================")
            print("      CHAT SESSION ENDED")
            print("===================================")
            break

start_chatbot()