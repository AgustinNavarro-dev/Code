### Programacion orientada a objetos

- Super clase: Clase en donde se pueden unificar todos los elementos del programa. Se ejecuta el programa en la super clase. (Figuras).
El metodo "main" suele ser la super clase. Es donde corre todo el programa
- Clase: Figuras geometricas, Figuras de accion. Se toma la herencia de la super clase.
- Objetos: Puede estar dentro de una clase o una super clase. Elementos que contienen atributos y metodos.
- Atributos: En el caso del rectangulo sería la base y la altura.
- Metodos: El rectangulo a travez de un metodo tendria la posibilidad de calcular su area. Por ejemplo multiplincado su base por su altura.
 Vendría a ser un conjunto de instrucciones.

### Arreglos / array
Es como una variable, puede ser texto o numeros, etc
- Unidimensionales: arreglo[5] se puede mover izq derecha
- Bidimensionales: arreglo[3][3] se puede mover izq derecha arriba abajo

### Como leer files
- En una string podemos usar el "/n" dentro y cuando usemos "print", va a haber un espacio ahi. Y cuenta como un solo character, no dos.

## Lists
- Cuando usamos "split" para dividir una string y convertirla en una lista,  
debemos usar un delimitador ejemplo linea.split(";"), porque sino  
lo que sucede es que delimita con los espacios, y si usamos muchos  
espacios, solo nos cuenta como uno.

## Dictionarys
- The Python dictionary is one of its most powerful data structures.  Instead of representing values in a linear list, dictionaries store data as key / value pairs.  Using key / value pairs gives us a simple in-memory "database" in a single Python variable.
- Dictionaries are like lists except that they used keys instead of numbers  
to look up values
- One common use of dictionaries is counting how often we "see" something
- We can use the "in" operator too se if a "key" is in the dictionary (money in bag)
- Podemos pedir una lista del diccionario, tambien de valores y de keys

## Tuples
-  Tuples are our third and final basic Python data structure. Tuples are a simple  
version lists. We often use tuples in conjuction with dictionaries to accomplish  
multi-step task like sorting or looping thought all of the data in a dictionary
- No podemos modificar las tuples, como se hace con las listas
- Son similares a las listas solo que se usan parantesis en vez de esto []
- Ocupan menos espacio en memoria, asi que es buena idea usarlas cuando vamos a  
usar variables temporales.
- Las tuplas son comparables
- Podemos usar el metodo items() para convertir el diccionario en tuple y despues usar sort() para acomodarlo.

## Lista comprehension
- Es una forma de acomodar listas. Puedo investigar un poco de eso mas tarde.
