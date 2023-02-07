class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length**2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


shape = Shape()
print("Area of Shape:", shape.area())

square = Square(5)
print("Area of Square:", square.area())

rectangle = Rectangle(5, 10)
print("Area of Rectangle:", rectangle.area())
