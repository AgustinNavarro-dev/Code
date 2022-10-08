#esto sirve para encontrar la palabra mas grande y cuantas veces se repite
#es bastante util

fileName = input("Ingrese el nombre del archivo: ")
handle = open(fileName)
counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

#este segmento es muy importante, usamos el valor key y value
# es una buena forma para hacer dos iteraciones, ya que si no lo hacemos de esta
# forma, no podemos tener valores ordenados
 = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)
