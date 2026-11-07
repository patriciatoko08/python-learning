from fastapi import FastAPI
from pydantic import BaseModel
import ollama

app = FastAPI()


class Question(BaseModel):
    question: str


@app.get("/")
def home():
    return {"message": "Hello, my API is working!"}


@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"Hello, {name}!"}


@app.post("/ask")
def ask(body: Question):
    response = ollama.chat(
        model="llama3.2",
        messages=[{"role": "user", "content": body.question}],
    )
    return {"answer": response["message"]["content"]}