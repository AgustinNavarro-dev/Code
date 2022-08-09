Hours = input("Enter Hours:")
Rate = input("Enter rate:")

Hoursa = float(Hours)
Ratea = float(Rate)
pay = 0

def computepay(pay):
    if Hoursa <= 40:
        pay = Hoursa * Ratea
        return pay
    elif Hoursa > 40:
        pay = (40 * Ratea) + ((Hoursa - 40) * (Ratea * 1.5))
        return pay

print("Pay", computepay(pay))
