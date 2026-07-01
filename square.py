import turtle

# Create a screen window for drawing
window = turtle.Screen()
window.title("Turtle Square")

# Create a turtle object named "pen"
pen = turtle.Turtle()

# Loop 4 times to draw the 4 sides of a square
for _ in range(4):
    pen.forward(100)  # Move forward by 100 pixels
    pen.left(90)      # Turn left by 90 degrees

# Keep the window open until it is clicked
window.exitonclick()
