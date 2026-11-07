from fastapi import FastAPI
from pydantic import BaseModel
import ollama

app = FastAPI()


class Question(BaseModel):
    question: str


def ask_model(prompt: str) -> str:
    response = ollama.chat(
        model="llama3.2",
        messages=[{"role": "user", "content": prompt}],
    )
    return response["message"]["content"]


@app.get("/")
def home():
    return {"message": "Hello, my API is working!"}


@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"Hello, {name}!"}


@app.post("/ask")
def ask(body: Question):
    return {"answer": ask_model(body.question)}


@app.post("/ask-document")
def ask_document(body: Question):
    with open("document.txt") as f:
        document = f.read()

    prompt = (
        "Answer the question using only the document below. "
        "Use the facts in the document to give the best answer you can, "
        "even if the document states the reason or fact indirectly. "
        "Only say you don't know if the document has no relevant information at all.\n\n"
        f"Document:\n{document}\n\n"
        f"Question: {body.question}"
    )
    return {"answer": ask_model(prompt)}