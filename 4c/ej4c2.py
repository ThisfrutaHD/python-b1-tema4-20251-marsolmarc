"""
Enunciat:
Es demana crear una interfície "Vehicles" que tingui un mètode abstracte "drive".
A més, cal crear les classes concretes "Car" i "Bicycle" que implementin
la interfície "Vehicles".

El mètode "drive" ha d'imprimir "Driving a car" per a la classe "Car" i "Riding"
a bicycle" per a la classe "Bicycle".

Paràmetres:
     La classe Car i Bicycle no reben paràmetres.
        
Exemple:
     Entrada:
         car = Car()
         print(car.drive())

         bicycle = Bicycle()
         print(bicycle.drive())
     Sortida:
         Driving a car
         Riding a bicycle
"""

from abc import ABC, abstractmethod

# Write abstract class Vehicles here 
class Vehicles():
    def drive(self):
        # Write here your code
        pass

# Corret and overwrite class Car(Vehicles) here 
class Car():
    def drive(self):
        # Write here your code
        pass

# Corret and overwrite class Bicycle(Vehicles) here 
class Bicycle():
    def drive(self):
        # Write here your code
        pass


# Si vols provar el teu codi, descomenta les línies següents i executa l'script
# car = Car()
# print(car.drive())

# bicycle = Bicycle()
# print(bicycle.drive())
