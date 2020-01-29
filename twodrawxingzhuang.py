import turtle
side = int(raw_input("您想画一个几边形："))

angle = 360.0 / side
length = 400 / side
turtle.fillcolor("blue")
turtle.begin_fill()
for side in range(side):
    turtle.forward(length)
    turtle.right(angle)
turtle.end_fill()
turtle.done()
