counts = dict()
print("Escriba una frase")
line = input()
words = line.split()

for word in words:
    counts[word] = counts.get(word, 0) + 1

print(counts)
