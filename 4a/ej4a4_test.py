from ej4a4 import add_elapsed_time
from flake8.api import legacy as flake8


def test_add_elapsed_time():
    # Test con un diccionario vacío
    assert add_elapsed_time({}, "Juan", 8.6) == {"Juan": 8.6}, "add_elapsed_time does not return the correct value for input {}, 'Juan', 8.6. It should be {'Juan': 8.6}"

    # Test con un diccionario que ya tiene elementos
    my_dict = {"Juan": 9.5, "Peter": 14.2, "Sofia": 6.5, "Alex": 8.7}
    assert add_elapsed_time(my_dict, "Juan", 8.6) == {
        "Juan": 8.6,
        "Peter": 14.2,
        "Sofia": 6.5,
        "Alex": 8.7,
    }, "add_elapsed_time does not return the correct value for input {'Juan': 9.5, 'Peter': 14.2, 'Sofia': 6.5, 'Alex': 8.7}, 'Juan', 8.6. It should be {'Juan': 8.6, 'Peter': 14.2, 'Sofia': 6.5, 'Alex': 8.7}"

    # Test con una clave nueva
    my_dict = {"Juan": 9.5, "Peter": 14.2, "Sofia": 6.5, "Alex": 8.7}
    assert add_elapsed_time(my_dict, "Lucas", 11.2) == {
        "Juan": 9.5,
        "Peter": 14.2,
        "Sofia": 6.5,
        "Alex": 8.7,
        "Lucas": 11.2,
    }, "add_elapsed_time does not return the correct value for input {'Juan': 9.5, 'Peter': 14.2, 'Sofia': 6.5, 'Alex': 8.7}, 'Lucas', 11.2. It should be {'Juan': 9.5, 'Peter': 14.2, 'Sofia': 6.5, 'Alex': 8.7, 'Lucas': 11.2}"

    # Test con un valor actualizado
    my_dict = {"Juan": 9.5, "Peter": 14.2, "Sofia": 6.5, "Alex": 8.7}
    assert add_elapsed_time(my_dict, "Juan", 10.2) == {
        "Juan": 10.2,
        "Peter": 14.2,
        "Sofia": 6.5,
        "Alex": 8.7,
    }, "add_elapsed_time does not return the correct value for input {'Juan': 9.5, 'Peter': 14.2, 'Sofia': 6.5, 'Alex': 8.7}, 'Juan', 10.2. It should be {'Juan': 10.2, 'Peter': 14.2, 'Sofia': 6.5, 'Alex': 8.7}"


def test_pep8_conformity():
    style_guide = flake8.get_style_guide()
    report = style_guide.check_files([
        "ej4a4.py",
    ])

    assert report.get_statistics("F") + report.get_statistics("E9") == [], ( #type: ignore
        "Your code does not comply with flake8. Please review your code"
    )
