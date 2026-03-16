Women's Day AI Chatbot

An AI-powered chatbot built with FastAPI that generates Women's Day quotes in multiple styles such as **short, poetic, and motivational**.
The chatbot uses an LLM through the Agno Agent framework with HuggingFace models to generate dynamic responses.

The application also includes a **simple web-based chat interface** where users can interact with the bot in real time.

---

# Features

* AI-powered chatbot for Women's Day
* Generates quotes in different styles

* Supports:

  * Short quotes
  * Poetic quotes
  * Motivational quotes
  * General questions
* Simple browser-based chat UI
* FastAPI backend for high performance

---

# Project Structure

```
Womens-Day-Chatbot/
│
├── main.py
├── templates/index.html
├── static/(css/js)
├── requirements.txt
├── .gitignore
└── README.md
```

### File Description

| File               | Description                                       |
| ------------------ | ------------------------------------------------- |
| `main.py`          | Main FastAPI application containing chatbot logic |
| `requirements.txt` | Python dependencies                               |
| `.gitignore`       | Files ignored by Git                              |
| `README.md`        | Project documentation                             |

---

# Requirements

* Python **3.12**
* HuggingFace API key

---

# Installation

Clone the repository:

```bash
git clone https://github.com/danzinfo/Womens-Day-Chatbot.git

cd Womens-Day-Chatbot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

This installs the following libraries:

* **FastAPI** – backend API framework
* **Uvicorn** – ASGI server for running FastAPI
* **Agno** – AI agent framework
* **Pydantic** – request validation models
* **Bindufy** – agent deployment tooling

---

# Environment Setup

Set your HuggingFace API key:

### Linux / Mac

```bash
export HF_API_KEY="your_api_key"
```

### Windows

```powershell
set HF_API_KEY=your_api_key
```

---

# Running the Application

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

The server will run at:

```
http://localhost:8000
```

---

# Web Chat Interface

Open your browser and navigate to:

```
http://localhost:8000
```

You will see a simple chat interface where you can ask for quotes such as:

* **"Give me a short women's day quote"**
* **"Give me a poetic women's day quote"**
* **"Give me a motivational women's day quote"**

The chatbot will respond accordingly.

---

# API Endpoint

## POST `/chat`

Send a message to the chatbot.

### Request

```json
{
  "message": "Give me a motivational women's day quote"
}
```

### Response

```json
{
  "response": "Empowered women inspire generations to rise."
}
```

---

# Technologies Used

* Python 3.12
* FastAPI
* Uvicorn
* Agno Agent Framework
* HuggingFace LLM
* Pydantic
* Bindufy

---

# Author

**Danzinfo**
📧 [danzinfo@gmail.com](mailto:danzinfo@gmail.com)

---

