"""
Enunciat:
Es demana crear una interfície "Animal" que tingui un mètode abstracte "talk".
A més, cal crear les classes concretes "Dog", "Cat" i "Parrot" que
implementin la interfície "Animal".

El mètode "talk" ha d'imprimir "Guau!" per a la classe "Dog", "Meow!"
per a la classe "Cat" i "Whistle!" per a la classe "Parrot"

Paràmetres:
     La classe Animal:
         - name: String que representa el nom de lanimal.
        
Exemple:
     Entrada:
         dog = Dog("Fido")
         dog.talk()

         cat = Cat("Fido")
         cat.talk()
        
         parrot = Parrot("Polly")
         parrot.name
     Sortida:
         "Guau!"
         "Meow!"
         "Polly"        
"""
# Write abstract class Animal here

# Corret and overwrite class Dog(Animal) here 
class Dog():
    def __init__(self, name):
        self.name = name

    def talk(self):
        pass

# Corret and overwrite class Cat(Animal) here 
class Cat():
    def __init__(self, name):
        self.name = name
    def talk(self):
        pass

# Corret and overwrite class Parrot(Animal) here 
class Parrot():
    def __init__(self, name):
        self.name = name
    def talk(self):
        pass





# Si vols provar el teu codi, descomenta les línies següents i executa l'script

def test_code():
	animals = [Dog("Fido"), Cat("Felix"), Parrot("Polly")]	
	for animal in animals:
	    print(f"{animal.name} dice {animal.talk()}")

#test_code()