import ollama

with open("document.txt") as f:
    document = f.read()

print("Ask questions about the document. Type 'quit' to stop.")

while True:
    question = input("\nQuestion: ")
    if question.lower() == "quit":
        break

    prompt = (
        "Answer the question using only the document below. "
        "Use the facts in the document to give the best answer you can, "
        "even if the document states the reason or fact indirectly. "
        "Only say you don't know if the document has no relevant information at all.\n\n"
        f"Document:\n{document}\n\n"
        f"Question: {question}"
    )

    response = ollama.chat(
        model="llama3.2",
        messages=[{"role": "user", "content": prompt}],
    )
    print(response["message"]["content"])