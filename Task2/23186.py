print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = ( x <= y) or z or not w
                if f:
                    print(x, y, z, w)