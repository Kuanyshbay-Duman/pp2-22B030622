import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)


p1 = Point(1, 2)
p2 = Point(4, 6)

p1.show()
p2.show()

p1.move(3, 4)
p1.show()

print("Distance between p1 and p2:", p1.dist(p2))
