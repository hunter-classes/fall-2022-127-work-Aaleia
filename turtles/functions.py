import turtle

def square(t,x,y,w,color,sidelen):
  # set the location, color, and width
  t.penup()
  t.goto(x,y)
  t.width(w)
  t.color(color)
  t.pendown()
  # draw a square
 
  for i in range(4):
    t.forward(sidelen)
    t.right(90)

def triangle(t,x,y,w,color,sidelen):
  t.penup()
  t.goto(x,y)
  t.width(w)
  t.color(color)
  t.pendown()
  for i in range(3):
    t.forward(sidelen)
    t.right(120)

def ngon(t,x,y,w,color,sidelen):
  t.penup()
  t.goto(x,y)
  t.width(w)
  t.color(color)
  t.pendown()
  for i in range (n):
    t.forward(sidelen)

wn = turtle.Screen()

crush = turtle.Turtle()
square(crush,0,0,5,"green",80)
triangle(crush,0,0,5,"purple",100)

squirt = turtle.Turtle()
square(squirt,100,100,5,"red",50)

square(crush,-50,30,3,"blue",100)
crush.setheading(45)
square(crush,100,30,2,"purple",60)

wn.exitonclick()
wn.mainloop()