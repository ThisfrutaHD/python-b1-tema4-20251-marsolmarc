import pytest
from ej4c2 import Car, Bicycle, Vehicles
from flake8.api import legacy as flake8


class TestVehicles:
    def test_drive_car(self):
        car = Car()
        assert car.drive() == "Driving a car", "Car.drive() should return 'Driving a car'"

    def test_drive_bicycle(self):
        bicycle = Bicycle()
        assert bicycle.drive() == "Riding a bicycle", "Bicycle.drive() should return 'Riding a bicycle'"

    def test_drive_vehicles_abstract_method(self):
        with pytest.raises(TypeError):
            vehicle = Vehicles()
            vehicle.drive()

    def test_drive_car_instance_of_vehicles_class(self):
        car = Car()
        assert isinstance(car, Vehicles), "Car should be an instance of Vehicles"

    def test_drive_bicycle_instance_of_vehicles_class(self):
        bicycle = Bicycle()
        assert isinstance(bicycle, Vehicles), "Bicycle should be an instance of Vehicles"


def test_pep8_conformity():
    style_guide = flake8.get_style_guide()
    report = style_guide.check_files([
        "ej4c2.py",
    ])

    assert report.get_statistics("F") + report.get_statistics("E9") == [], ( #type: ignore
        "Your code does not comply with flake8. Please review your code"
    )
    