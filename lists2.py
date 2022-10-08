## usar find con una lista

fhand = open("mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    if not line.startswith("From ") : continue
    words = line.split()
    print(words[2])
    #con esto, lo que hago es buscar directamente esa palabra
