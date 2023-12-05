# Import the turtle module, which allows drawing on the screen
import turtle

# Create a turtle named 'artist' and a screen named 'my_screen'
artist = turtle.Turtle()
artist.speed(0)  # 0 is the fastest speed
my_screen = turtle.Screen()

# Set the background color of the turtle screen
turtle.bgcolor("indigo")

# Draw the chain
artist.penup()
artist.goto(0, 250)
artist.pendown()
artist.color("darkkhaki")
artist.pensize(10)
artist.right(90)
artist.forward(100)

# Draw the attachment
artist.pensize(1)
artist.right(90)
artist.back(20)
artist.begin_fill()
for i in range(2):
    artist.forward(40)
    artist.left(90)
    artist.forward(10)
    artist.left(90)
artist.end_fill()

# Draw the red bauble
artist.penup()
artist.goto(0, 140)
artist.pendown()
artist.color("crimson")
artist.begin_fill()
artist.circle(200)
artist.end_fill()

# Draw the gold zigzag
artist.penup()
artist.goto(176, 30)
artist.pendown()
artist.color("gold")
artist.pensize(3)
artist.left(45)
for i in range(5):
    # Draw a segment of the zigzag pattern
    artist.forward(50)
    artist.right(90)
    artist.forward(50)
    artist.left(90)

# Draw the green circles
artist.penup()
artist.goto(-160, -65)
artist.pendown()
artist.color("limegreen")
artist.left(135)
artist.begin_fill()
for i in range(5):
    # Draw a green circle
    artist.circle(10)
    # Move to the next position for the next circle
    artist.penup()
    artist.forward(80)
    artist.pendown()
artist.end_fill()

# Draw the second gold zigzag
artist.penup()
artist.goto(-185, -135)
artist.pendown()
artist.color("gold")
artist.left(45)
for i in range(5):
    # Draw a segment of the second zigzag pattern
    artist.forward(50)
    artist.right(90)
    artist.forward(50)
    artist.left(90)
# Move to the starting position of the bottom line
artist.forward(35)

# Draw stars at the top
artist.penup()
artist.goto(-105, 80)
artist.pendown()
artist.pensize(1)
artist.color("aliceblue")
artist.setheading(0)
# for i in range(3):
#     # Draw a star
#     artist.begin_fill()
#     for i in range(5):
#         artist.forward(30)
#         artist.right(144)
#     artist.end_fill()
#     # Move to the next position for the next star
#     artist.penup()
#     artist.forward(90)
#     artist.pendown()

# # Draw stars at the bottom
# artist.penup()
# artist.goto(-105, -180)
# artist.pendown()
# artist.setheading(0)
# for i in range(3):
#     # Draw a star
#     artist.begin_fill()
#     for i in range(5):
#         artist.forward(30)
#         artist.right(144)
#     artist.end_fill()
#     # Move to the next position for the next star
#     artist.penup()
#     artist.forward(90)
#     artist.pendown()

# Write a festive message on the screen
artist.penup()
artist.goto(-180, 270)
artist.pendown()
artist.color("white")
artist.write("SEASONS GREETINGS", font=("Arial", 24, "bold"))

# Close the window when clicked
my_screen.exitonclick()
