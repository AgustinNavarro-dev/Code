#loop
n = 0
while n < 5:
    print(n)
    n = n + 1
print("fin")

#break y continue usando if condition:

while True:
    line = input("> ")
    if line[0] == "continue":
        continue
    if line == "done":
        break
    print(line)
print("done")

#for loop
for n in [5, 4, 3, 2]:
    print(n)
print("FIN")

#como encontrar el numero mas largo usando loop
largestnumber = 0
for number in [2, 4, 9, 2, 12, 33, 1]:
    if number > largestnumber:
        largestnumber = number
print(largestnumber)

#encontrar el numero mas chico usando loop y None(otro tipo de variable)
numerochico = None
for number in [2, 4, 9, 2, 12, 33, 2]:
    if numerochico is  None:  #"is" y "is not", son operadores que van con None
        numerochico = number  # "is" es mas poderoso que "==" porque tambien compara el tipo
    elif number < numerochico: # de variable (int, float, etc)
        numerochico = number
print(numerochico)

#la forma de hacer un Contador en loop
counter = 0
print("Before", counter)
for thing in [2, 3, 5, 98, 23, 42, 44, 2, 0, 1]:
    counter = counter + 1
    print("Now ", counter, thing)
print("Contador: ", counter)

#como sumar las variables de una lista por ej en un loop
suma = 0
for cosas in [2, 34, 2, 32, 65, 1 ,1, 6]:
    suma = cosas + suma
    print(suma, cosas)
print("Sumatoria: ", suma)

#promedio loop usando suma y contador
suma = 0
counter = 0
for cosas in [3, 4, 2, 90, 34, 62, 12, 42, 11]:
    suma = cosas + suma
    counter = counter + 1
    print(suma, counter, cosas)
print("Suma: ", suma, "Counter: ", counter, "Average: ", suma/counter)

#filtering

print("Before")
for num in [2, 32, 2, 56, 12, 23, 14, 11, 8]:
    if num > 20:
        print("larger number: ", num)
print("After")

#search using a boolean
found = False
for num in [12, 43, 11, 6, 44, 2, 9]:
    if num == 11:
        found = True
        #aca podemos poner un "BREAK" y se termina con el loop
    print(found, num)
