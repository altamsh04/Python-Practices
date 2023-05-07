import math

class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def surface_area(self):
        return 2 * math.pi * self.radius * self.height + 2 * math.pi * self.radius ** 2

    def volume(self):
        return math.pi * self.radius ** 2 * self.height


c = Cylinder(3, 5)
print("Surface area of cylinder:", c.surface_area())
print("Volume of cylinder:", c.volume())
