#looping a string
fruit = "banana"
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

#contador de letras en una string

word = "banana"
counter = 0
for letter in word:
    if letter == "a" :
        counter = counter + 1
print(counter)

#de esta forma puedo cortar strings
a = "Agustin Navarro"
print(a[0:7])  #puedo eliminar el primer o segundo numero [:x] [x:] y va hasta o desde
print(a[8:10])

#"in" sirve para saber si un caracter o una cadena esta dentro de una cadena
fruta = "banana"
if "a" in fruta:
    print("True")

#estas son formas de convertir a minuscula las mayusculas
string = "Hola Mundo"
lower = string.lower() #esta funcion no modifica el string (lanza uno nuevo)
print(lower)
print("Hola MUNDO".lower())
#tambien existe la funcion upper.()

#variable strings
variable = "string"
dir(variable)#puedo ver que funciones puedo utilizar


#funcion replace() lo que hace es remplazar ("esto", "por esto")
cadena = "Hola Mundo"
reemplazada = cadena.replace("Mundo", "Agustin")
print(reemplazada)

#funcion find() busca una cadena de caracteres y si  no la encuentra
#lanza un -1
#si la encuentra lanza la posicion

hola = "Soy un humano"
pos = hola.find("humano")
print(pos)

#funcion lstrip() and rstrip() borra los espacios a la derecha o izquierda
#funcion strip() borra todo
saludo = " Hola, Mundo "
print(saludo.rstrip())
print(saludo.strip())

#funcion startswith() te devuelve un true or false si empieza con cierto strings
hola = "Hola"
hola.startswith("H")

#como buscar data con find().
data = "From navarroagustin1993@gmail.com Sat Jan 2022"
atpos = data.find("@")
print(atpos) #imprime la posicion
spos = data.find(" ", atpos) #coloco el atpos para indicar que busque el espacio
#despues del "@"
print(spos)
print(data[atpos + 1 : spos])
