# Use the file name mbox-short.txt as the file name
count = 0
total = 0
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("File cannot be opened: ", fname)
    quit()

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1  #este contador me sirve para sacar el promedio
    inpos = line.find(':')
    total = total + float(line[inpos+2:])
    avg = total / count
print("Average spam confidence:", avg)


#no se porque no funciona el try. algun dia lo averiguare
