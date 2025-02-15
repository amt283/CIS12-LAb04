import turtle
import random

"""PUT YOUR FUNCTIONS HERE"""
def draw_square(t, length):
    """Draws a square with the given side length."""
    for _ in range(4):
        t.forward(length)
        t.left(90)

def draw_circle(t, radius):
    """Draws a circle with the given radius."""
    t.circle(radius)

def draw_polygon(t, sides, length):
    """Draws a regular polygon with a given number of sides and side length."""
    angle = 360 / sides
    for _ in range(sides):
        t.forward(length)
        t.left(angle)

def jump(t: turtle.Turtle, x, y):
    """Moves turtle to another location (x,y) on the screen
    without drawing a continuous line then uses pendown to start drawing again"""
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_pumpkin(t, x, y, radius):
    """Draws a pumpkin (orange circle) at the given (x, y) location with a green stem."""
    jump(t, x, y)
    t.fillcolor("orange")
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

    # Drawing the stem
    # y has "radius // 10" subtracted to lower stem to a more natural looking spot
    jump(t, x+(radius // 10), y+2*radius-(radius // 10))
    t.fillcolor("green")
    t.begin_fill()
    t.left(90)  # Point upwards
    t.forward(radius // 2)
    t.left(90)
    t.forward(radius // 5)
    t.left(90)
    t.forward(radius // 2)
    t.left(90)
    t.forward(radius // 5)
    t.end_fill()

def draw_eye(t, x, y, size):
    """Draws one triangular eye at the given (x, y) position."""
    jump(t, x, y)
    t.fillcolor("yellow")
    t.begin_fill()
    draw_polygon(t, 3, size)
    t.end_fill()

def draw_mouth(t, x, y, width):
    """Draws a jagged mouth using a series of connected lines."""
    jump(t, x, y)
    t.fillcolor("yellow")
    t.begin_fill()
    t.right(60)
    for _ in range(5):  # Create a simple zigzag mouth
        t.forward(width // 5)
        t.left(120)
        t.forward(width // 5)
        t.right(120)
    t.left(60)
    t.end_fill()

def draw_star(t, x, y, size):
    """Draws a star at the given (x, y) position."""
    jump(t, x, y)
    t.fillcolor("white")
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)  # 144 degrees is the angle to form a star
    t.end_fill()

def draw_sky(t, num_stars):
    """Draws a starry sky with the given number of stars."""
    for _ in range(num_stars):
        x = random.randint(-300, 300)
        y = random.randint(0, 300)
        size = random.randint(10, 30)
        draw_star(t, x, y, size)

def draw_jack(t, x, y, radius):
    draw_pumpkin(t, x, y, radius)
    eye_height = y+((1/2)*(2*radius))
    eye_size = (.3)*radius
    mouth_height = eye_height - (1/2)*radius
    draw_eye(t, x-((1/2)*radius), eye_height, eye_size)
    draw_eye(t, x+((1/4)*radius), eye_height, eye_size)
    draw_mouth(t, x-((.45)*radius), mouth_height, radius)  # Mouth

# Create a turtle object
t = turtle.Turtle()

# Hide the turtle and set speed
t.speed(10)  # 1 is slow, 10 is fast, 0 is instant
t.hideturtle()

# Create a window to draw in
# Create a new turtle screen and set its background color
screen = turtle.Screen()
screen.bgcolor("darkblue")
# Set the width and height of the screen
screen.setup(width=600, height=600)
# Clear the screen
t.clear()

"""PUT YOUR DRAW CALLS TO FUNCTIONS HERE"""
t.color("#F05E16") # Dark orange line color, for Halloween!

# Draw three jack-o-lanterns
draw_jack(t, -150, -150, 100)
draw_jack(t, 0, -150, 80)
draw_jack(t, 150, -150, 100)

# # Draw the night sky
draw_sky(t, 30)

# Close the turtle graphics window when clicked
turtle.exitonclick()