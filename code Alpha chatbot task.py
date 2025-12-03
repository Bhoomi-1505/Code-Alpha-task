def chatbot():
    print(" Chatbot: Hello! Type 'bye' to end the chat.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Chatbot: Hi!")
        
        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!")
        
        elif user_input in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye!")
            break
        
        else:
            print("Chatbot: Sorry, I didn't understand that.")

# Run the chatbot
chatbot()