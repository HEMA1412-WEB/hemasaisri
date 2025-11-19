def chatbot():
    print("Hello! I'm your friendly chatbot.")
    print("Type 'bye' anytime to end the chat.\n")

    while True:
        user_input = input("You: ").lower()

        if "hello" in user_input:
            print("Bot: Hi there!")
        elif "how are you" in user_input:
            print("Bot: I'm doing great, thanks for asking!")
        elif "your name" in user_input:
            print("Bot: I'm ChatBuddy, your simple chatbot assistant.")
        elif "bye" in user_input:
            print("Bot: Goodbye! Have a nice day!")
            break
        else:
            print("Bot: Sorry, I didn't understand that.")

if __name__ == "__main__":
    chatbot()
