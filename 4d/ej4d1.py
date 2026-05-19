"""
Enunciat:
Realitzant l'entrada per consola de les dades, implementa la funció 'sum'
que sol·liciti l'entrada de dos números amb 'input' i torni la suma dels
números.

Paràmetre:5
No rep cap paràmetre pel fet que dins de la funció se sol·licita la
entrada dels números.

Exemple:
     Entrada:
         "Insert the first number: " 8
         "Insert the second number: " 3

     Sortida:
         "Result: " 11
"""

def sum():
    num_1 = int(input("Insert the first number: "))
    num_2 = int(input("Insert the second number: "))
    result = num_1 + num_2
    print("Resultat: ", result)
    return result

# Si vols provar el teu codi, descomenta les línies següents i executa l'script
sum()
