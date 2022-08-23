#CON ESTO LO QUE ESTOY HACIENDO ES LEER E IMPRIMIR TODO EL TEXTO
fh = open("mbox-short.txt")
for lx in fh:
    ly = lx.rstrip() #con este comando elimino el ultimo caracter de cada renglon
    #el ultimo era el salto de linea, para que solo haya uno, y no dos.
    print(ly.upper()) #con este comando convierto todo en mayus
