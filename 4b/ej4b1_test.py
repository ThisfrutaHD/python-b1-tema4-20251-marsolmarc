import pytest
from flake8.api import legacy as flake8

from ej4b1 import squared_sum_ram, squared_sum_heap


def test_squared_sum_ram():
    numbers_list = [6, 4, 7]
    expected_result = 101
    assert squared_sum_ram(numbers_list) == expected_result, "squared_sum_ram does not return the correct value for input [6, 4, 7]. It should be 101"


def test_squared_sum_heap():
    numbers_list = [6, 4, 7]
    expected_result = 101
    assert squared_sum_heap(numbers_list) == expected_result, "squared_sum_heap does not return the correct value for input [6, 4, 7]. It should be 101"


def test_pep8_conformity():
    style_guide = flake8.get_style_guide()
    report = style_guide.check_files([
        "ej4b1.py",
    ])

    assert report.get_statistics("F") + report.get_statistics("E9") == [], ( #type: ignore
        "Your code does not comply with flake8. Please review your code"
    )
    