# word_counter
text = "i love python and python is motivation."
words = text.split()
counts= {}
for word in words:
    if word in counts:
        counts[word] = counts[word] + 1
    else:
        counts[word] = 1
for word, counts in counts.items():
    print(f"{word}  → {counts} times")