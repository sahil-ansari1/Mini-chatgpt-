# 🤖 Mini ChatGPT — Your Personal AI CLI Assistant

A minimal Python-based chatbot that uses OpenAI's GPT-3.5-Turbo to chat with you directly in your terminal.  
Fast, lightweight, and super easy to set up — perfect for learning and productivity.

---

## ✨ Features

- 🧠 Talk to ChatGPT right from your terminal
- ⚙️ Clean and minimal Python code
- 🔐 API key securely stored via `config.py`
- 💬 Unlimited conversation flow (until you type `exit`)
- 🛠️ Easy to modify and extend as per your need

---

## ⚙️ Installation & Setup (Everything in One Go)

### 1. Install Required Package

```bash
pip install openai

2. Clone the Project

git clone https://github.com/sahilansari-dev/mini-chatgpt.git
cd mini-chatgpt

3. Add Your API Key

Edit the config.py file and paste your API key like this:

# config.py
API_KEY = "your_openai_api_key_here"

👉 You can get your key from: https://platform.openai.com/account/api-keys

4. Run the Chatbot

python chatgpt.py


---

💬 Example Usage

Welcome to your Personal AI Chatbot! (type 'exit' to quit)
You: Hello!
Bot: Hi there! How can I help you today?

You: Write a short poem.
Bot: Roses are red, violets are blue...


---

📂 Project Structure

mini-chatgpt/
│
├── chatgpt.py     # Main chatbot logic
├── config.py      # Stores your API key
└── README.md      # You're reading it now!


---

⚠️ Notes

If your API quota ends, just change the API key in config.py.

Don’t expose your key publicly.

Feel free to customize:

Add message history

Save chat to a file

Use different GPT models




---

👨‍💻 Author

Sahil Ansari
Made with ❤️ by a curious Python enthusiast exploring AI and automation.
🔗 GitHub: github.com/sahilansari-dev


---

📜 License

This project is open-source and free to use under the MIT License.

---



