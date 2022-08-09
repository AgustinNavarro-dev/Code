number = input("Enter just a number:")

#se usa try cuando suponemos que algo puede fallar
#es una especie de seguro
try:
    numberConv = int(number)
except:
    numberConv = -1
if numberConv >= 0:
    print("Good job")
else:
    print("Not a number")
