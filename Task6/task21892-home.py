from turtle import *

screensize(100, 100)
tracer(0)
m=10

rt(90)
for i in range(7):
    rt(45)
    fd(11*m)
    rt(45)
up()
for x in range(-10, 20):
    for y in range(-10, 20):
        goto(x*m, y*m)
        dot(3, 'red')
update()
done()
#113