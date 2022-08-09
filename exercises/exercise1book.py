num = 0
total = 0
while True:
    sval = input("Ingrese un numero: ")
    if sval == "Done":
        break
    try:
        fval = float(sval)
    except:
        print("Valor incorrecto")
    num = num + 1
    total = total + fval
print(total, num, total/num)
