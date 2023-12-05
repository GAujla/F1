# Import the turtle module, which allows drawing on the screen
import turtle

# Create a turtle named 'artist' and a screen named 'my_screen'
artist = turtle.Turtle()
my_screen = turtle.Screen()

# Set the drawing speed, background color, and pen size
artist.speed(0)  # 0 is the fastest speed
turtle.bgcolor("black")
artist.pensize(2)

# Draw the wreath with circles in different shades of green
artist.penup()
artist.goto(0, -100)
artist.pendown()
for i in range(13):
    for colours in ["forestgreen", "darkgreen", "limegreen"]:
        artist.color(colours)
        artist.circle(150)
        artist.left(10)
        artist.forward(20)

# Draw a ribbon bow using red color
artist.penup()
artist.goto(-95, 110)
artist.pendown()
artist.color("darkred", "red")
artist.begin_fill()
artist.forward(200)
artist.right(120)
artist.forward(100)
artist.right(120)
artist.forward(200)
artist.left(120)
artist.forward(100)
artist.end_fill()

# Draw a circle in the middle of the ribbon
artist.penup()
artist.goto(-40, 160)
artist.pendown()
artist.begin_fill()
artist.circle(30)
artist.end_fill()

# Draw left dangly part of the ribbon
artist.penup()
artist.goto(-25, 132)
artist.pendown()
artist.begin_fill()
artist.right(20)
artist.forward(130)
artist.left(80)
artist.forward(60)
artist.left(118)
artist.forward(150)
artist.end_fill()

# Draw right dangly part of the ribbon
artist.begin_fill()
artist.right(92)
artist.forward(5)
artist.right(80)
artist.forward(150)
artist.left(110)
artist.forward(60)
artist.left(89)
artist.forward(139)
artist.end_fill()

# Draw yellow decorations
artist.penup()
artist.goto(-150, 20)
artist.pendown()
artist.color("gold", "yellow")
artist.begin_fill()
artist.circle(10)
artist.end_fill()

artist.penup()
artist.goto(120, 110)
artist.pendown()
artist.begin_fill()
artist.circle(10)
artist.end_fill()

# Draw red decorations
artist.penup()
artist.goto(140, 40)
artist.pendown()
artist.color("darkred", "red")
artist.begin_fill()
artist.circle(10)
artist.end_fill()

artist.penup()
artist.goto(-135, 110)
artist.pendown()
artist.begin_fill()
artist.circle(10)
artist.end_fill()

# Write a Christmas message on the screen
artist.penup()
artist.goto(-170, 250)
artist.pendown()
artist.color("white")
artist.write("MERRY CHRISTMAS", font=("Arial", 25, "bold"))

artist.penup()
artist.goto(-215, -250)
artist.pendown()
artist.write("AND A HAPPY NEW YEAR", font=("Arial", 25, "bold"))

# Close the window when clicked
my_screen.exitonclick()
