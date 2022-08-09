def greet(lang):        #se pueden usar diversos parametros
    if lang == "es":
        return "Hola"   #con return devolvemos el "hola" usando la funcion
    elif lang == "en":  #la funcion termina cuando aparece RETURN
        return "Hello"
    else:
        return "Hola motherfucker"
print(greet("es"), "Agu")   #si se usa otro parametro no tira error
                            #puedo usar una variable int sin problemas

#podemos agregar mas parametros
def suma(a, b):
    total = a + b
    return total
print(suma(3, 6), "es el total")

#otro ejemplo de como usar un parametro
def imprimirParametro(x):
    print(x)
imprimirParametro("hola")
imprimirParametro("mundo")
