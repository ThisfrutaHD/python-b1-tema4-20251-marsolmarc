"""
Enunciat:

Implementa la classe "Shape", que té el mètode 'get_sides', que torna una
llista amb els costats de la forma.

Després, implementa la classe "Triangle", que hereta de "Shape" i té els mètodes
'area' i '__init__', on el mètode 'area' torna l'àrea del triangle i '__init__'
inicialitza els atributs base, altura i costats de la forma.

Finalment, implementa la classe "Rectangle", que hereta de "Shape" i té els
mètodes 'area' i '__init__', on el mètode 'area' torna l'àrea del rectangle
i '__init__' inicialitza els atributs longitud, ample i costats de la forma.

Paràmetres:
     Per a la classe Triangle:
         - sides: una llista de tres enters, que representa els costats del
         triangle.
         - base: un nombre enter, que representa la base del triangle.
         - height: un nombre enter, que representa l'alçada del triangle.
    
     Per a la classe Rectangle:
         - sides: una llista de quatre enters, que representa els costats del
         rectangle.
         - length: un nombre enter, que representa el llarg del rectangle.
         - width: un nombre enter, que representa l'amplada del rectangle.
        
Exemple:
     Entrada:
         triangle = Triangle([3, 4, 5], 4, 3)
         triangle.area()
        
         rectangle = Rectangle([5, 5, 2, 2], length=5, width=2)
         rectangle.get_area()
     Sortida:
         6.0
         10        
"""

# Corret and overwrite class Dog(Shape) here
class Shape:
    def __init__(self, sides):
        self.sides = sides

    def get_sides(self):
        return self.sides
    
# Corret and overwrite class Triangle(Shape) here
class Triangle():
    def __init__(self, sides, base, height):        
        pass

    def get_area(self):
        pass

# Corret and overwrite class Rectangle(Shape) here
class Rectangle(Shape):
    def __init__(self, sides, length, width):        
        pass

    def get_area(self):
        pass


# Si vols provar el teu codi, descomenta les línies següents i executa l'script

# # Create a triangle with base 4 and height 3
#triangle = Triangle([3, 4, 5], base=4, height=3)
# # Get the area of the triangle
#print(triangle.get_area()) # Output: 6.0
#print (triangle.get_sides()) # shows sides of the triangle

# # Create a rectangle with length 5 and width 2
#rectangle = Rectangle([5, 5, 2, 2], length=5, width=2)
# # Get the area of the rectangle
#print(rectangle.get_area()) # Output: 10
#print (rectangle.get_sides()) # shows sides of the rectangle
