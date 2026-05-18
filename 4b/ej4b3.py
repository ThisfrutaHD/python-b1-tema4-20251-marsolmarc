"""
Enunciat:

Implementa una funció anomenada 'create_list(length_list)' que rebi de
paràmetre un valor numèric enter anomenat 'length_list'. Cal retornar
dues llistes d'enters que il·lustrin l'emmagatzematge de valors a la RAM
i al Heap. Per tant, la primera llista ha de tenir números enters
aleatoris entre 0 i 100, que ha de ser emmagatzemada a la RAM; i la
segona llista ha de ser emmagatzemada al Heap reutilitzant la primera llista
creada.

Per crear una llista al Heap, es pot fer servir la llibreria 'copy' i la seva funció
'deepcopy(list)', en aquest exemple el farem servir de la següent forma:
“copy.deepcopy('list_to_copy')”.

Per crear números aleatoris es pot fer servir la llibreria 'random'. Hauràs de
afegir "import random" al teu codi, i després utilitzar "random.randint(0, 100)"
per crear números aleatoris entre 0 i 100.

Considerar que en cas que el número 'length_list' ingressat a la funció
'create_list' s'ha de mostrar l'error:
ValueError("The number must be positive")

Paràmetres:
     - length_list (int): Número enter que sigui positiu.

Exemple:
     Entrada:
     create_list(4)

     Sortida:
     ([17, 16, 30, 17], [17, 16, 30, 17])

"""
import copy
import random


def create_list(length_list):
    """
    Creates two lists of integers to illustrate the difference between RAM and
    Heap memory.

    Args:
    length_list: A numeric integer value indicating the length of the lists to
    be created.

    Returns:
    A tuple containing two lists of integers, the first one created in RAM and
    the second one created in Heap by reusing the first list.
    """
    
    if length_list < 0:
        raise ValueError("The number must be positive")

    llista_ram = []
    for _ in range(length_list):
        llista_ram.append(random.randint(0, 100))
    
    llista_heap = copy.deepcopy(llista_ram)

    return llista_ram, llista_heap


# Si vols provar el teu codi, descomenta les línies següents i executa l'script
print(create_list(6))
