import turtle
from math import sin, cos, pi
turtle.speed(3)
turtle.shape('turtle')
x = 0
y = 0
Vx = 5
Vy = 20
dt = 1
for _ in range(300):
    x += Vx*dt
    Vy -= dt
    y += Vy*dt + 5*dt**2
    if 0 <= y and y<= Vx*dt:
        Vy = -0.9*Vy
    turtle.goto(x,y)

turtle.exitonclick()

