from ej4a3 import descending_list_iterator
from flake8.api import legacy as flake8


def test_descending_list_iterator():
    # Test with an empty list
    assert list(descending_list_iterator([])) == [], "descending_list_iterator does not return the correct value for input []. It should be [], that is, empty"

    # Test with a list of one element
    assert list(descending_list_iterator([5])) == [5], "descending_list_iterator does not return the correct value for input [5]. It should be [5]"

    # Test with a list of multiple elements
    assert list(descending_list_iterator([5, 1, 8, 3, 2])) == [8, 5, 3, 2, 1], "descending_list_iterator does not return the correct value for input [5, 1, 8, 3, 2]. It should be [8, 5, 3, 2, 1]"

    # Test with a list of repeated elements
    assert list(descending_list_iterator([2, 2, 2, 2, 2])) == [2, 2, 2, 2, 2], "descending_list_iterator does not return the correct value for input [2, 2, 2, 2, 2]. It should be [2, 2, 2, 2, 2]"

    # Test with a list of negative numbers
    assert list(descending_list_iterator([-5, -1, -8, -3, -2])) == [-1, -2, -3, -5, -8], "descending_list_iterator does not return the correct value for input [-5, -1, -8, -3, -2]. It should be [-1, -2, -3, -5, -8]"


def test_pep8_conformity():
    style_guide = flake8.get_style_guide()
    report = style_guide.check_files([
        "ej4a3.py",
    ])

    assert report.get_statistics("F") + report.get_statistics("E9") == [], ( #type: ignore
        "Your code does not comply with flake8. Please review your code"
    )
