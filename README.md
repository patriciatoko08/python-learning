# Python Learning

Hi, I'm Patricia TOKO. I have a Higher Technician Diploma in Software Engineering (IAI Cameroon) and I'm now learning Python to specialize in AI application development.

This repository contains my first Python projects.

## Projects

| File | What it does |
|------|--------------|
| `hello.py` | My first program: asks for a name and greets the user |
| `calculator.py` | Calculates sum, difference and product, with error handling |
| `word_count.py` | Reads a text file and shows the 5 most common words |
| `weather.py` | Shows the current weather for any city, using a public API |
| `todo.py` | Command-line to-do list that saves tasks in a file |
| `ask_ai.py` | Sends a question to a local AI model (Ollama) |
| `chatbot.py` | Chatbot that remembers the conversation |

## How to run

You need Python 3 installed. For the weather program, install the `requests` library first:

```
pip3 install requests
python3 weather.py
```

For the AI programs, install [Ollama](https://ollama.com), then run these commands once:

```
pip3 install ollama
ollama pull llama3.2
```

Then run `python3 chatbot.py`.

## What I practiced

- Python basics: variables, loops, functions, dictionaries
- Reading and writing files, including JSON
- Error handling with `try/except`
- Calling a REST API with `requests`
- Running a local AI model and building a chatbot with memory
- Git and GitHub

## Next

- Asking an AI model questions about a text file
- Calling a cloud AI API such as Claude's
- Building a small web API with FastAPI