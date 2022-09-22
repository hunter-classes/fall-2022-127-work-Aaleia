import turtle

wn = turtle.Screen()
crush = turtle.Turtle()

# draw a square

crush.width(5)
crush.color("purple")

crush.forward(50)
crush.right(90)
crush.forward(50)
crush.right(90)
crush.forward(50)
crush.right(90)
crush.forward(50)
crush.right(90)

squirt = turtle.Turtle()

# draw a triangle

squirt.up()
squirt.goto(0,100)
squirt.down()
squirt.width(5)
squirt.color("red")

squirt.forward(50)
squirt.right(120)
squirt.forward(50)
squirt.right(120)
squirt.forward(50)
squirt.right(120)

wn.exitonclick()
wn.mainloop()