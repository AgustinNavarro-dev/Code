fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    words = line.split()
    lst.extend(words) # USO EXTEND PORQUE SI USO APPEND,
    # CREO OTRA LISTA NUEVA DENTRO DE LA INICIAL
print(lst)
