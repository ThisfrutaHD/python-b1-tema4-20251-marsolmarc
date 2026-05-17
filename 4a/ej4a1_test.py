from ej4a1 import find_intersection
from flake8.api import legacy as flake8


def test_find_intersection():
    lista1 = [1, 2, 3, 4, 5]
    lista2 = [4, 5, 6, 7, 8]
    resultado = find_intersection(lista1, lista2)
    assert resultado == {4, 5}, "find_intersection does not return the correct value for input ([1, 2, 3, 4, 5], [4, 5, 6, 7, 8]). It should be [4, 5]"

    lista3 = [1, 2, 3]
    lista4 = [4, 5, 6]
    resultado = find_intersection(lista3, lista4)
    assert resultado == set(), "find_intersection does not return the correct value for input ([1, 2, 3], [4, 5, 6]). It should be an empty list []"

    lista5 = []
    lista6 = [1, 2, 3]
    resultado = find_intersection(lista5, lista6)
    assert resultado == set(), "find_intersection does not return the correct value for input ([], [1, 2, 3]). It should be an empty list []"


def test_pep8_conformity():
    style_guide = flake8.get_style_guide()
    report = style_guide.check_files([
        "ej4a1.py",
    ])

    assert report.get_statistics("E") == [], (
        "Your code does not comply with flake8. Please review your code"
    )