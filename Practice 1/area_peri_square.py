class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side


s = Square(5)
print("Area of square:", s.area())
print("Perimeter of square:", s.perimeter())
