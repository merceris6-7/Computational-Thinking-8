import turtle

t = turtle.Turtle()

t.goto(100, 0)
#Turtle color is red
t.color("red")
#screen color is black
turtle.Screen().bgcolor("black")

#turtle movement
for i in range(5):
    t.forward(100)
    t.left(72)

for i in range(6):
    t.forward(100)
    t.left(60)

for i in range(12):
    t.forward(100)
    t.left(50)

for i in range(6):
    t.forward(100)
    t.left(44)

for i in range(6):
    t.forward(100)
    t.left(74)

for i in range(6):
    t.forward(100)
    t.left(60)

for i in range(6):
    t.forward(100)
    t.left(61)

turtle.exitonclick()
