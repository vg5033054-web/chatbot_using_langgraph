# 🤖 LangGraph AI Chatbot

<p align="center">
  <b>An intelligent conversational AI built with LangGraph, LangChain, and Streamlit.</b>
  <br/>
  A simple yet powerful chatbot with conversation history and interactive chat experience.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/LangGraph-1C3C3C?style=for-the-badge" alt="LangGraph"/>
  <img src="https://img.shields.io/badge/LangChain-121212?style=for-the-badge&logo=chainlink&logoColor=white" alt="LangChain"/>
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit"/>
</p>

---

## ✨ About the Project

**LangGraph AI Chatbot** is a conversational AI application developed using Python and the LangGraph framework. It uses a graph-based workflow to process user messages and generate AI responses.

The chatbot features a Streamlit interface that makes interacting with the AI simple and user-friendly.

This project demonstrates how to build an AI chatbot using modern LLM application development tools.

## 🚀 Features

- 💬 **Interactive Chat Interface** — Chat with AI through a clean Streamlit UI.
- 🧠 **LangGraph Workflow** — Process conversations using a graph-based architecture.
- 📝 **Conversation History** — Display previous messages during the current Streamlit session.
- ⚡ **Real-Time Interaction** — Submit messages and receive AI-generated responses.
- 🔧 **Modular Architecture** — Keep chatbot logic separate from the user interface.
- 🌱 **Extendable Design** — Add memory, tools, RAG, and other AI capabilities in the future.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| LangGraph | Manages the chatbot workflow |
| LangChain | Provides LLM integration and message handling |
| Streamlit | Builds the interactive web interface |
| LLM Provider | Generates conversational responses |

## 📂 Project Structure

```text
langgraph-chatbot/
│
├── app.py                 # Streamlit chatbot interface
├── langgraph_backend.py   # LangGraph workflow and chatbot logic
├── requirements.txt       # Project dependencies
├── .env                   # API keys and environment variables
├── .gitignore             # Files excluded from Git
└── README.md              # Project documentation
```

*Note: Update the filenames above to match your actual repository.*

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root and add the API key required by your selected LLM provider.

```env
YOUR_API_KEY=your_api_key_here
```

Replace the example variable with the exact variable name expected by your backend code. Never publish real API keys on GitHub.

### 5. Run the chatbot

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal to start chatting with your AI assistant.

## 🧠 How It Works

```text
       User Message
            |
            v
     Streamlit Interface
            |
            v
      LangGraph Workflow
            |
            v
      Chatbot / LLM Node
            |
            v
       AI Response
            |
            v
     Chat Interface
```

1. The user enters a message in the Streamlit interface.
2. The application passes the message to the LangGraph workflow.
3. The chatbot node processes the input using the configured language model.
4. The generated response is returned to Streamlit.
5. The interface displays the conversation.

## 🔮 Future Improvements

- [ ] Persistent conversation memory
- [ ] Multiple conversation threads
- [ ] Support for multiple LLM providers
- [ ] Streaming AI responses
- [ ] Retrieval-Augmented Generation (RAG)
- [ ] AI tools and agent capabilities
- [ ] Deployment with Streamlit Community Cloud

## 🔐 Security

- Keep API keys in environment variables.
- Add `.env` to `.gitignore`.
- Never commit passwords, API tokens, or private credentials.
- If a secret is accidentally pushed, revoke or rotate it immediately.

## 🎯 Learning Outcomes

Through this project, I explored:

- Building conversational AI applications with Python.
- Creating workflows using LangGraph.
- Integrating language models with LangChain.
- Developing interactive applications with Streamlit.
- Managing conversation history and application state.

## 👨‍💻 Author

**Mo. Sahil**

AI & Machine Learning Enthusiast | Python Developer | Exploring Generative AI and Agentic AI

<p align="center">
  ⭐ If you find this project useful, consider giving it a star!
  <br/>
  💡 Suggestions and contributions are welcome.
</p>

---

<p align="center">
  <b>Built with Python, LangGraph, and a passion for AI. 🚀</b>
</p>
