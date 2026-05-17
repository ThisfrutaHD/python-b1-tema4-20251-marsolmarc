"""
Enunciat:

Escriu una funció anomenada 'descending_list_iterator(numbers_list)' que prengui una llista
de números com a argument i torni un iterador que generi els mateixos
nombres de més gran a més petit.

Paràmetres:
     numbers_list (list): Llista de nombres enters a ser ordenats.

Exemple:
     Entrada:
     [5, 1, 8, 3, 2]

     Sortida:
     L'iterador hauria de generar els números en l'ordre següent:
     8, 5, 3, 2, 1.

"""


def descending_list_iterator(numbers_list):
    numbers_list.sort(reverse=True)
    return iter(numbers_list)


# Si vols provar el teu codi, descomenta les línies següents i executa l'script

numeros = [2, 3, 6, 9, 11, 12, 15, 18, 67]
print(list(descending_list_iterator(numeros)))  

def descending_list_iterator_manual(numbers_list):
    # Ordenar manualment (bubble sort descendent)
    for i in range(len(numbers_list)):
        for j in range(len(numbers_list) - 1):
            if numbers_list[j] < numbers_list[j + 1]:
                # intercanvi
                temp = numbers_list[j]
                numbers_list[j] = numbers_list[j + 1]
                numbers_list[j + 1] = temp

    # crear iterador manualment
    return iter(numbers_list)


print(list(descending_list_iterator_manual(numeros)))