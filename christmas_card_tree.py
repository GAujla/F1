# Import the turtle module
import turtle

# Create a screen for drawing
my_screen = turtle.Screen()

# Set the background color to light blue
turtle.bgcolor("light blue")

# Create a turtle named 'artist' for drawing
artist = turtle.Turtle()

# Set the shape of the turtle to look like a turtle
#artist.shape("turtle")

# Draw the tree trunk
artist.penup()
artist.goto(-20, -150)
artist.color("brown")
artist.begin_fill()
artist.fillcolor("brown")

artist.pendown()
# Draw a rectangle to represent the tree trunk
artist.forward(40)
artist.right(90)
artist.forward(50)
artist.right(90)
artist.forward(40)
artist.right(90)
artist.forward(50)
artist.end_fill()

# Move to the left to draw the tree's leaves
artist.penup()
artist.goto(-100, -150)
artist.right(90)
artist.color("green")
artist.begin_fill()
artist.fillcolor("green")

artist.pendown()
# Draw an equilateral triangle to represent the tree's leaves
artist.forward(200)
artist.left(120)
artist.forward(200)
artist.left(120)
artist.forward(200)
artist.end_fill()

# Draw the ornaments on the tree

# First ornament
artist.penup()
artist.right(190)
artist.forward(50)
artist.color("blue")
artist.begin_fill()
artist.fillcolor("blue")
# Draw a circle to represent the first ornament
artist.circle(10)
artist.end_fill()

# Second ornament
artist.penup()
artist.forward(100)
artist.begin_fill()
# Draw a larger circle to represent the second ornament
artist.circle(15)
artist.end_fill()

# Third ornament
artist.penup()
artist.right(120)
artist.forward(100)
artist.begin_fill()
# Draw a circle to represent the third ornament
artist.circle(10)
artist.end_fill()

# Fourth ornament
artist.penup()
artist.right(110)
artist.forward(60)
artist.color("red")
artist.begin_fill()
artist.fillcolor("red")
# Draw a circle to represent the fourth ornament
artist.circle(10)
artist.end_fill()

# Fifth ornament
artist.penup()
artist.right(110)
artist.forward(60)
artist.begin_fill()
# Draw a circle to represent the fifth ornament
artist.circle(10)
artist.end_fill()

# Sixth ornament
artist.penup()
artist.right(110)
artist.forward(75)
artist.begin_fill()
# Draw a larger circle to represent the sixth ornament
artist.circle(20)
artist.end_fill()

# Seventh ornament
artist.penup()
artist.right(180)
artist.forward(30)
artist.begin_fill()
# Draw a circle to represent the seventh ornament
artist.circle(10)
artist.end_fill()

# Move to the top to write "Merry Christmas"
artist.penup()
artist.goto(0, 100)
artist.color("black")
artist.write("Merry Christmas", align="center", font=("Arial", 30, "bold"))

# Hide the turtle and close the drawing when clicked
artist.hideturtle()
my_screen.exitonclick()
