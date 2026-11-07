import ollama
from datetime import datetime

question = input("Ask something: ")

now = datetime.now().strftime("%A %d %B %Y, %H:%M")

prompt = (
    f"Today's date and time is {now}. "
    f"Use this information to answer the question.\n\n"
    f"Question: {question}"
)

response = ollama.chat(
    model="llama3.2",
    messages=[{"role": "user", "content": prompt}],
)

print(response["message"]["content"])