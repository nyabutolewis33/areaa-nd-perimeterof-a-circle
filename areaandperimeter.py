import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius
circle = Circle(56)

print("Area of the circle:", circle.area())
print("Perimeter of the circle:", circle.perimeter())