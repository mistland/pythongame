import turtle
length = 100
angle = 90
chang = 10
jiao = 1
"""�ҹ�������"""
turtle.forward(length)
turtle.right(angle)
turtle.forward(length)
turtle.right(angle)
turtle.forward(length)
turtle.right(angle)
turtle.forward(length)
"""���"""
turtle.left(angle)
turtle.forward(length)
turtle.left(angle)
turtle.forward(length)
turtle.left(angle)
turtle.forward(length)
turtle.right(angle)
"""����"""
turtle.forward(100)
turtle.right(angle)
while chang < 200:
    turtle.forward(chang)
    turtle.right(90)
    chang = chang + 10
"""��Բ"""
while jiao < 360:
    turtle.forward(1)
    turtle.right(1)
    jiao = jiao + 1
    
    

