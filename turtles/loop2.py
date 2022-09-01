import turtle

def sample_function():
    print("This is a function!")
    print("It can be used multiple times.")

wn = turtle.Screen()
crush = turtle.Turtle()
squirt = turtle.Turtle()

# draw a triangle

squirt.up()
squirt.goto(-5,5)
squirt.down()
squirt.width(5)
squirt.color("blue")
for i in range(3):
    squirt.forward(50)
    squirt.right(120)

sample_function()

wn.exitonclick()
wn.mainloop()