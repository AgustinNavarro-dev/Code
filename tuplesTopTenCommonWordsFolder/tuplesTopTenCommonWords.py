#aca usamos listas, diccionarios y tuples
#el objetivo de este codigo es ordenar por VALUE
#esto se consigue dando vuelta los valores, ordenando y volver a darlos vuelta
#ya que si solo usamos sort, ordena por key, no por value

fhand = open("cuento.txt")
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) +1
#aca lo que hicimos fue cortar las lineas del texto y colocarlas en una lista

lst = list()
for key, val in counts.items():
    newSetUp = (val,key)
    lst.append(newSetUp)
lst = sorted(lst, reverse=True)
print(lst)

#con esto logramos intercambiar valor por key, darlos vuelta, y meterlos
#a una lista

for val, key in lst[:10]:
    print(key, val)
