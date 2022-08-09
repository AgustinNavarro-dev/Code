hrs = input("Enter Hours:")
rate = input("Rate:")
try:
    r = float(rate)
    h = float(hrs)
except:
    print("Error. Please enter numeric input")
    quit()
total = 0
if h <= 40:
    total = h * r
elif h > 40:
    total = (h - 40) * 10.5 * 1.5 + 40 * 10.5
else:
    print("Error")
print(total)
