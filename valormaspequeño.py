numerochico = None
for number in [2, 4, 9, 2, 12, 33, 2]:
    if numerochico is  None:
        numerochico = number
    elif number < numerochico:
        numerochico = number
print(numerochico)
