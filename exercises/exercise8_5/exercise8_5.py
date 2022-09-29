fname = input ("Ingrese el nombre del file: ")
fh = open(fname)
for line in fh:
    line = line.rstrip()
    if not line.startswith("From:") : continue
    mails = line.split()
    # tambien puedo usar esto:
    #if mails[0] != "From:" :
    #    continue (en vez del if not line.sta...)
    print(mails[1])

#
#con esto leo el texto y tambien se como mostrar solo los mails
