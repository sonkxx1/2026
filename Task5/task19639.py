for N in range(1,100000):
    R = f'{N:b}'
    if R.count('0') % 2 == 0:
        R = '1' + R + '1'
    else