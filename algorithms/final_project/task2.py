import turtle


def draw_pythagoras_tree(t, length, level):
    if level == 0:
        t.forward(length)
        t.backward(length)
    else:
        t.forward(length)
        t.left(45)
        draw_pythagoras_tree(t, length * 0.7, level - 1)
        t.right(90)
        draw_pythagoras_tree(t, length * 0.7, level - 1)
        t.left(45)
        t.backward(length)


def main():
    screen = turtle.Screen()
    screen.title("Pythagoras Tree")

    # Prompt user for the level of recursion
    level = int(
        screen.textinput(
            "Level of Recursion", "Enter the level of recursion (e.g., 5):"
        )
    )

    t = turtle.Turtle()
    t.speed(0)  # Fastest speed
    t.left(90)  # Start facing upwards
    t.penup()
    t.goto(0, -200)  # Move to a better starting position
    t.pendown()

    draw_pythagoras_tree(t, 100, level)

    screen.mainloop()


if __name__ == "__main__":
    main()
