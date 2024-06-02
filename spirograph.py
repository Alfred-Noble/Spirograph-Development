import turtle as t
import random
timmy = t.Turtle()

t.colormode(255)
timmy.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color_need = (r, g, b)
    return random_color_need


def draw_spirograph(size_gap):
    for _ in range(int(360 / size_gap)):
        timmy.color(random_color())
        timmy.circle(50)
        timmy.setheading(timmy.heading() + size_gap)


draw_spirograph(2)

screen = t.Screen()
screen.exitonclick()
