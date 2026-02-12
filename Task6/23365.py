from turtle import *

screensize(3000,3000)
tracer(0)
m = 15

for i in range(3):
    fd(39*m)
    rt(90)
    fd(48*m)
    rt(90)
up()
fd(27*m)
rt(90)
fd(24*m)
lt(90)
down()
for i in range(3):
    fd(29*m)
    rt(90)
    bk(18*m)
    rt(90)
up()
for x in range(0,13):
    for y in range(-42,-23):
        goto(x*m, y*m)
        dot(3,'red')
update()
done()
#2178