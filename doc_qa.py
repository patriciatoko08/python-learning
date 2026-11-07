import ollama

with open("document.txt") as f:
    document = f.read()

question = input("Ask about the document: ")

prompt = (
    "Answer the question using only the document below. "
    "If the answer is not in the document, say you don't know.\n\n"
    f"Document:\n{document}\n\n"
    f"Question: {question}"
)

response = ollama.chat(
    model="llama3.2",
    messages=[{"role": "user", "content": prompt}],
)

print(response["message"]["content"])