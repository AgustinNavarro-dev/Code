def computepay(h, r):
    total = 0
    if h <= 40:
        total = h * r
    elif h > 40:
        total = (h - 40) * 10.5 * 1.5 + 40 * 10.5
    else:
        print("Error")
    return total

h = input("Ingrese la cantidad de horas: ")
h = float(h)
r = input("Ingrese el rate: ")
r = float(r)
print(computepay(h, r))
