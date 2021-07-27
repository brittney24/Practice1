import turtle
t = turtle.Turtle()
for i in range(8):
  for c in ['red', 'green', 'yellow', 'blue', 'purple']:
    t.color(c)
    t.forward(9)
    t.left(45)
    t.forward(9)
    t.right(35)
    t.forward(9)


t.pu()
t.goto(-75,170)
t.pd()
for i in ['red', 'green', 'yellow', 'blue', 'purple']:
  t.color(i)
  t.forward(100)
  t.right(144)
