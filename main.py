import pgzrun
import math
WIDTH = 600
HEIGHT = 800
RADIUS = 25

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    def __str__(self):
        return f"({self.x}, {self.y}"

class Paddle:
    pass

class Circle:
    def __init__(self, vector: Vector):
        self.position = vector
        self.velocity = Vector(100, 200)


circle = Circle(Vector(200,200))
def draw():
    screen.clear()
    screen.draw.circle((circle.position.x, circle.position.y), RADIUS, 'white')

def update(dt):
    v = circle.velocity
    if circle.position.y >= HEIGHT - RADIUS and v.y > 0:
        circle.velocity = Vector(v.x, -v.y)
    elif circle.position.y <= RADIUS and v.y < 0:
        circle.velocity = Vector(v.x, -v.y)

    elif circle.position.x >= WIDTH - RADIUS and v.x > 0:
        circle.velocity = Vector(-v.x, v.y)
    elif circle.position.x <= RADIUS and v.x < 0:
        circle.velocity = Vector(-v.x, v.y)
    circle.position += Vector(v.x * dt, v.y * dt)



pgzrun.go()
