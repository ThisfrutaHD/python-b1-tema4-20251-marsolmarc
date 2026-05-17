"""
Enunciat:
Donades dues llistes d'elements, implementa una funció anomenada
find_intersection(list_1, list_2) que retorni la intersecció de les dues llistes.

Paràmetres:
     list_1 (List): Llista d'elements
     list_2 (List): Llista d'elements

Exemple:
     Entrada:
     list_1 = [1, 2, 3, 4, 5]
     list_2 = [4, 5, 6, 7, 8]

     Sortida:
     [4, 5]

"""

list_1 = [1, 2, 3, 4, 5]
list_2 = [4, 5, 6, 7, 8]


def find_intersection(list_1, list_2):
    set_1 = set(list_1)
    set_2 = set(list_2)
    interseccio = set_1 & set_2
    return interseccio


def find_intersection_without_function(list_1, list_2):
     resultat = []

     for x in list_1:
          if x in list_2 and x not in resultat:
               resultat.append(x)
     return resultat


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script

#print(find_intersection([1, 2, 3, 4], [3, 4, 5, 6]))
#print(find_intersection(['apple', 'banana', 'orange'], ['banana', 'kiwi', 'apple']))
