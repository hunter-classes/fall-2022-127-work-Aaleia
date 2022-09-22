import turtle

# draw a hexagon
def hexagon(t,x,y,w,color,sidelen):
  t.penup()
  t.goto(x,y)
  t.width(w)
  t.color(color)
  t.pendown()
  for i in range (6):
    t.forward(sidelen)
    t.right(60)

# draw a regular ngon with nsides
def ngon(t,numsides,x,y,w,color,sidelen):
  t.penup()
  t.goto(x,y)
  t.width(w)
  t.color(color)
  t.pendown()
  for i in range (numsides):
    t.forward(sidelen)
    t.right(360/numsides)

wn = turtle.Screen()

crush = turtle.Turtle()
hexagon(crush,50,50,5,"blue",100)
ngon(crush,8,20,20,5,"purple",80)

wn.exitonclick()
wn.mainloop()