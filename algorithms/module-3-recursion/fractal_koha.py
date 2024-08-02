import turtle
import argparse


def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        # for angle in [60, -120, 60, 0]:
        #    koch_curve(t, order - 1, size / 3)
        #    t.left(angle)
        koch_curve(t, order - 1, size / 3)
        t.left(60)
        koch_curve(t, order - 1, size / 3)
        t.right(120)
        koch_curve(t, order - 1, size / 3)
        t.left(60)
        koch_curve(t, order - 1, size / 3)


def draw_koch_curve(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    window.mainloop()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Enter the level of order")
    parser.add_argument("--order", type=int, default=3, help="Koch fractal level")
    args = parser.parse_args()

    order = args.order
    draw_koch_curve(order)
