from turtle import *

tracer(0)
screensize(2000,2000)
m = 10

for i in range(4):
    fd(36*m)
    rt(90)
    fd(41*m)
    rt(90)
up()
rt(90)
fd(20*m)
lt(90)
fd(20*m)
down()
for i in range(4):
    fd(25*m)
    rt(90)
up()
fd(7*m)
lt(90)
fd(7*m)
rt(90)
down()
for i in range(7):
    fd(16*m)
    rt(90)
up()
for x in range(-10,70):
    for y in range(-50,40):
        goto(x*m,y*m)
        dot(3,'red')
update()
done()