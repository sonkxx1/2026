for N in range(1,100_000):
    R = f'{N:x}'
    if R.count('b') % 2 == 0:
        R = '1' + R
    else:
        R += 1
    R = int(R, 16)
    if 10<= R <= 99:
        if len(str(R)) == 2:
            if sum([1 for i in str(R)]) == 2 :
                

