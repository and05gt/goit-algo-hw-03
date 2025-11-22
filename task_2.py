import turtle

def koch_curve(t, order, size):
    """Recursively draws one Koch curve."""

    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_snowflake(order, size=400):
    """Draws a Koch snowflake of a given order and size."""

    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.color("blue")
    t.speed(0)
    t.hideturtle()
    t.penup()
    t.goto(-size / 2, size / (2 * 1.732))
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)
    
    window.mainloop()

if __name__ == "__main__":
    try:
        recursion_level = int(input("Enter the recursion level (0-6): "))

        if 0 <= recursion_level <= 6:
            draw_koch_snowflake(recursion_level, size=400)
        else:
            print("Please enter a valid recursion level between 0 and 6.")
    
    except ValueError:
        print("Invalid input. Please enter an integer between 0 and 6.")
    except Exception as e:
        print(f"An error occurred: {e}")