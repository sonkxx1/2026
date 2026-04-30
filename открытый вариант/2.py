print('x y z w')
for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            for w in range(0,2):
                f = ((z<=x)<=(x==y)) or(not w)
                if not f:
                    print(x,y,z,w)
#  w