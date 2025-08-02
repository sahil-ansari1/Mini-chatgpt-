import openai
from config import OPENAI_API_KEY

# OpenAI key set karo
openai.api_key = OPENAI_API_KEY

# Chatbot se sawaal poochhne ka function
def ask_chatbot(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # agar tu free plan pe hai
        messages=[
            {"role": "system", "content": "You are a helpful study assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']

# Main chatbot loop
def main():
    print("Welcome to your Personal AI Chatbot! (type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        reply = ask_chatbot(user_input)
        print("Bot:", reply)

if __name__ == "__main__":
    main()