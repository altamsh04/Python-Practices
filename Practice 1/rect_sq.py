class Shape:
    def area(self, length, breadth=None):
        if breadth is None:
            return length ** 2
        else:
            return length * breadth


shape = Shape()

print("Area of square with side 5 is:", shape.area(5))

print("Area of rectangle with length 4 and breadth 6 is:", shape.area(4, 6))
