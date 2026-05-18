"""
Enunciat:
Implementa la funció 'squared_sum_ram(numbers_list)' que rep una llista de números
enters i calculeu la suma dels seus valors al quadrat. Cal utilitzar un bucle 'for'
per il·lustrar l'ús de la RAM.

La funció 'squared_sum_heap(numbers_list)' ja està implementada i ha d'emmagatzemar la
suma dels valors al quadrat al Heap. No obstant això, hi ha un error en aquest càlcul 
identifica'l i corregeix-lo.

Paràmetres:
     - numbers_list: Llista de nombres enters.

Exemple:
     Entrada:
     squared_sum_ram([6, 4, 7])
     squared_sum_heap([6, 4, 7])

     Sortida:
     101
     101

"""


def squared_sum_ram(numbers_list):
    suma_quadrat = 0
    for num in numbers_list:
        suma_quadrat += num**2
    return suma_quadrat


def squared_sum_heap(numbers_list):
    # Store the list in Heap
    # You should correct and overwrite something in the following line.
    squared_sum_list = [num**2 for num in numbers_list]
    heap_sum = sum(squared_sum_list)
    return heap_sum


# # Si vols provar el teu codi, descomenta les línies següents i executa l'script
numbers_list = [6, 4, 7]
print(squared_sum_ram(numbers_list))
print(squared_sum_heap(numbers_list))
