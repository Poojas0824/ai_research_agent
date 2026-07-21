# 🤖 AI Research Agent (Beginner Project)

This is a simple AI Research Agent built using LangChain + Google Gemini + Tools (Wikipedia + Web Search + File Save).

It takes a user query, searches information from the web/Wikipedia, and returns a structured research output.

---

 🚀 Features

- 🔍 Web search using DuckDuckGo
- 📚 Wikipedia search integration
- 💾 Save results to a text file
- 🤖 Powered by Google Gemini (LangChain)
- 📊 Structured output using Pydantic

---

🛠️ Tech Stack

- Python 🐍
- LangChain 🧠
- Google Gemini (ChatGoogleGenerativeAI)
- Wikipedia API
- DuckDuckGo Search
- Pydantic (for structured output)

---
 📁 Project Structure


project/
│
├── main.py # Main AI agent logic
├── tools.py # Custom tools (search, wiki, save)
├── requirements.txt # Dependencies
└── .env # API keys


---
 ⚙️ Installation

 1. Clone the project
```bash
git clone https://github.com/Maaz708/ai_reseacrh_agent
cd ai_reseacrch_agent

2. Create virtual environment
python -m venv venv

Activate it:

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate
3. Install dependencies
pip install -r requirements.txt
4. Add API Key

Create a .env file:

GOOGLE_API_KEY=your_api_key_here
▶️ Run the Project
python main.py

Then enter your query:

What can i help you research?
