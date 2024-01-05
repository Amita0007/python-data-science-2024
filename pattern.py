from turtle import *
pensize(5)
pencolor('black')
speed('fast')
for i in range(6):
    fd(120)
    lt(360/6)
    circle(60, steps=6)
    write(i+1)
    for j in range(6):
        fd(60)
        lt(360/6)
hideturtle()
mainloop()
