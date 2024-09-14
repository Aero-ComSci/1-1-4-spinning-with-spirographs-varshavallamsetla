import turtle
import random

#800px
screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.title("Concentric Squares")

#turtle
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

def draw_square(size):
    """Draws a square of a given size."""
    for _ in range(4):
        t.forward(size)
        t.right(90)

def random_color():
    """Generate a random color."""
    return (random.random(), random.random(), random.random())

num_squares = int(input("Enter the number of squares to draw: "))
initial_size = 100
size_decrement = 10

#squares
for i in range(num_squares):
    size = initial_size - i * size_decrement
    t.color(random_color())
    t.penup()
    t.goto(-size / 2, size / 2)
    t.pendown()
    draw_square(size)

turtle.done()

