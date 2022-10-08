##buscar el avrga con una lista

numlist = list()
while True:
    inp = input("Enter a number: ")
    if inp == "done" : break
    value = float(inp)
    numlist.append(value)
average = sum(numlist) / len(numlist)

print(average)

## no se usa este metodo para grandes listas de numeros, ya que podrian
## llevar mucho espacio en memoria
## para 100 millones de numeros, por ej, se utilizaria una avrg normal
## se sumarian dos variables siempre y luego se dividirian.
