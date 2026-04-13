print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (x <= z) and y and (x or w)
                if f:
                    print(x,y,z,w)