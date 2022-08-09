suma = 0
counter = 0
for cosas in [3, 4, 2, 90, 34, 62, 12, 42, 11]:
    suma = cosas + suma
    counter = counter + 1
    print(suma, counter, cosas)
print("Suma: ", suma, "Counter: ", counter, "Average: ", suma/counter)
