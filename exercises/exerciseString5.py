#convertir el numero despues del colon character y pasarlo a float
str = "X-DSPI Confidence: 0.231321 "
pos1 = str.find(":")
pos2 = str.find(" ", pos1 + 2)
print(pos1, pos2)
number = float(str[pos1 +2 : pos2])
print(number)

#lo que hice fue cortar desde el ":" hasta el ultimo espacio
#pero tambien se puede hacer esto:

str = "X-DSPI Confidence: 0.231321 "
pos1 = str.find(":")
piece = str[pos1 + 2:] #si no coloco el final del string, lo lleva hasta el final
piece = float(piece)
print(piece)
