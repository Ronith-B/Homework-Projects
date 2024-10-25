import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Method to calculate the area of the circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Method to calculate the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius


circle = Circle(5)  
print("Area of the circle:", circle.area())
print("Perimeter of the circle:", circle.perimeter())
