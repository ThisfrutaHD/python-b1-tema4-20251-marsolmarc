"""
Enunciat:
Es necessita implementar les classes següents:

Classe "Person": Representa una persona i compta amb un mètode 'descriu(self)'
que torna una descripció de la persona.
Classe "Student": Representa un estudiant i té com a paràmetre la classe
"Person". A més, compta amb un mètode "descriu" que estén la descripció
de la persona i afegeix informació sobre la carrera que estudia.

Cal crear dos objectes, "person_1" i "student_1", a partir de les
classes "Person" i "Student", respectivament. Cal accedir als
mètodes 'descriu' dels objectes i mostrar la descripció corresponent.

El mètode 'descriu' de la classe "Person" retornarà el següent format:
f"{self.name} is {self.age} years old."

El mètode 'descriu' de la classe "Student" retornarà el mateix que la classe 
"Person" i, a més:
f"{description} Studies {self.major}."    

Paràmetres:
     Per a la classe Person:
         - name: String amb el nom de la persona/objecte.
         - age: un nombre enter que representa l'edat de la persona.
    
     Per a la classe Student:
         - name: String amb el nom de l'estudiant.
         - age: Un nombre enter que representa l'edat de l'estudiant.
         - major: String que indica la carrea que estudia.
        
Exemple:
     Entrada:
         person_1 = Person("Joan", 30)
         person_1.describe()
        
         student_1 = Student("Ana", 25, "Systems Engineering")
         student_1.describe()
     Sortida:
         Juan is 30 years old.
         Ana is 25 years old. Studies Systems Engineering.

"""

# Class that represents a person
class Person:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method that returns the description of the person
    def describe(self):
        # Write here your code
        pass


# Class that represents a student
class Student(Person):
    # Constructor
    def __init__(self, name, age, major):
        # Write here your code
        pass

    # Method that returns the description of the student
    def describe(self):
        # Write here your code
        pass


person_1 = Person("Juan", 30)
student_1 = Student("Ana", 25, "Systems Engineering")

# Si vols provar el teu codi, descomenta les línies següents i executa l'script

# Access to object methods
#print(person_1.describe())  # Juan is 30 years old.
#print(student_1.describe())  # Ana is 25 years old. Studies Systems Engineering.
