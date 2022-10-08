c = {"a":12, "u":23, "g": 33, "t": 2}   #diccionario
print(c)
tmp = list()
for k,v in c.items(): #c.items() convierte a tuples
    tmp.append((v,k)) #con esto damos vuelta el k por v y agregamos a la lista
print(tmp)
tmp = sorted(tmp, reverse=True) #acomodamos a la inversa
print(tmp)

# de todo esto obtenemos una lista con tuples acomodadas
