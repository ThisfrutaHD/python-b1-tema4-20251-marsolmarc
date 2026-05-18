import pytest
from ej4c3 import Triangle, Rectangle, Shape
from flake8.api import legacy as flake8


def test_triangle_get_area():
    triangle = Triangle([3, 4, 5], 4, 3)
    assert triangle.get_area() == 6.0, "Triangle.get_area() does not return the correct value for input [3, 4, 5], 4, 3. It should be 6.0"


def test_rectangle_get_area():
    rectangle = Rectangle([5, 5, 2, 2], 5, 2)
    assert rectangle.get_area() == 10, "Rectangle.get_area() does not return the correct value for input [5, 5, 2, 2], 5, 2. It should be 10"


def test_pep8_conformity():
    style_guide = flake8.get_style_guide()
    report = style_guide.check_files([
        "ej4c3.py",
    ])

    assert report.get_statistics("F") + report.get_statistics("E9") == [], ( #type: ignore
        "Your code does not comply with flake8. Please review your code"
    )
    