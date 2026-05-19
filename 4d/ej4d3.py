"""
Enunciat:

Implementa una funció 'read_and_write', no rep cap paràmetre a causa de
que, dins de la mateixa cal sol·licitar l'entrada de 2 dades mitjançant
teclat.

En el moment de sol·licitar l'ingrés de les dades s'ha de considerar el
següent text.
'Insert your name: ' El valor introduït ha de ser de tipus str.
'Insert your age: ' El valor introduït ha de ser de tipus int.

S'ha de crear un fitxer de text 'file.txt' on La informació entrada
per consola s'ha de guardar en aquest fitxer i s'ha d'imprimir per consola
des del fitxer de text.

Paràmetre:
No rep cap paràmetre.

Exemple:
     Entrada:
         'Insert your name: ' Juliol
         'Insert your age: ' 30
     Sortida:
         Juliol
         30

"""

def read_and_write():
    name = input("Insert your name: ")
    age = int(input("Insert your age: "))

    with open("file.text", "w") as f:
        f.write(f"{name}\n{age}")

    with open("file.text", "r") as fr:
        print(fr.read())


# Si vols provar el teu codi, descomenta les línies següents i executa l'script
read_and_write()
