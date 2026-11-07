import ollama

history = []

print("Chat with the AI. Type 'quit' to stop.")

while True:
    question = input("\nYou: ")
    if question.lower() == "quit":
        break

    history.append({"role": "user", "content": question})

    response = ollama.chat(model="llama3.2", messages=history)
    answer = response["message"]["content"]

    history.append({"role": "assistant", "content": answer})
    print(f"AI: {answer}")