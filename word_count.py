with open("text.txt") as f:
    text = f.read()

text = text.lower()

for mark in ".,!?;:\"'()":
    text = text.replace(mark, "")

words = text.split()

counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

top = sorted(counts.items(), key=lambda item: item[1], reverse=True)

for word, number in top[:5]:
    print(f"{word}: {number}")