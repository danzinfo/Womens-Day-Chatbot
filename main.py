from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from bindu.penguin.bindufy import bindufy
from agno.agent import Agent
from agno.models.huggingface import HuggingFace
import os


# --- Agent setup ---
agent = Agent(
    instructions="""
    You are a chatbot that celebrates Women's Day.
    - If asked for a short quote, respond with a one-liner
    - If asked for a poetic quote, respond in verse
    - If asked for a motivational quote, respond with a uplifting message
    - Otherwise, answer general questions helpfully
    """,
    model=HuggingFace(
        id="openai/gpt-oss-120b:groq",
        api_key=os.getenv("HF_API_KEY")
    )
)

# --- Agent config ---
config = {
    "author": "danzinfo@gmail.com",
    "name": "womens_day_agent",
    "description": "Chatbot agent that generates women's day quotes in different styles",
    "handler": "pdf-processing-v1",
    "version": "1.0.0",
    "capabilities": {},
    "auth": {"enabled": False},
    "storage": {"type": "memory"},
    "scheduler": {"type": "memory"},
    "deployment": {
        "url": "http://localhost:8000",
        "expose": True
    }
}

app = FastAPI()
templates=Jinja2Templates(directory="templates")


# Request schema
class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home(request:Request):
    return templates.TemplateResponse("index.html",{"request":request})


# --- Chat API ---
@app.post("/chat")
def chat(req: ChatRequest):
    user_input = req.message.lower()

    if "short" in user_input:
        reply = agent.run(input="Give me a short women's day quote")
    elif "poetic" in user_input:
        reply = agent.run(input="Give me a poetic women's day quote")
    elif "motivational" in user_input:
        reply = agent.run(input="Give me a motivational women's day quote")
    else:
        reply = agent.run(input=req.message)

    return {"response": reply.content}

