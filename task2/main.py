import turtle  # Import turtle graphics module

screen = turtle.Screen()
t = turtle.Turtle()

t.speed(0)      # Set the fastest drawing speed
t.hideturtle()   # Hide the turtle cursor

depth = int(input("Enter recursion level: "))  # Ask user for recursion depth

# Recursive function to draw one side of the Koch snowflake
def koch_side(n):
    if n == 0:
        t.forward(5)  # Base case: draw a straight line
    else:
        # Recursive case: split line into 4 segments with angles
        for angle in [60, -120, 60, 0]:
            koch_side(n-1)
            t.left(angle)

# Draw 3 sides to form the Koch snowflake
for _ in range(3):
    koch_side(depth)
    t.right(120)  # Turn 120 degrees to draw next side

screen.mainloop()  # Keep the window open
