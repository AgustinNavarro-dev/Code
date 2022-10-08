# counts = dict()
# names = ["Agustin", "Marino", "Navarro", "Agustin", "Monti", "Marino"]
# for name in names:
#     if name not in counts:
#         counts[name] = 1
#     else:
#         counts[name] = counts[name] + 1
# print(counts)

#PARA COMENTAR UNA SECCION ENTERA: CTRL + SHIFT + 7


# tambien se puede hacer usando "get"

counts = dict()
names = ["Agustin", "Marino", "Navarro", "Agustin", "Monti", "Marino"]
for name in names:
    counts[name] = counts.get(name, 0) +1
print(counts)
