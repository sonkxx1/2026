from turtle import *

screensize(3000, 3000)
tracer(0)
m = 30

for i in range(6):
    fd(33*m)
    rt(90)
    fd(20*m)
    rt(90)
up()
fd(3*m)
rt(90)
fd(9*m)
lt(90)
down()
for i in range(6):
    fd(24*m)
    rt(90)
    fd(25*m)
    rt(90)

up()
for x in range(-10,40):
    for y in range(-40,40):
        goto(x*m,y*m)
        dot(3,'red')
update()
done()