#con file() podemos abrir un file. no abrirlo, pero si acceder a el
#con open() lo abrimos "handle = open(filename, mode)" filename: diario.txt
#mode: con "r" leemos, y con "w" escribimos
#con /n vamos a otra linea, se usa adentro de strings "Hola /n mundo"


#es una forma de buscar palabras en un file
xfile = open("mbox.txt")
for cheese in xfile:
    print(cheese)

#como contar lineas
fhand = open("mbox.txt")
count = 0
for line in fhand:
    count = count + 1
print('Line count', count)
