from math import log2, ceil
#1855
L = 101
N = 4090 + 10
i = ceil(log2(N))
I = ceil(L * i/ 8)
print(I * 2048/2**10)
#23270
for L in range(1,100000):
    N = 27 + 10
    i = ceil(log2(N))
    I = ceil(L * i/ 8)
    if 3538*I> 12* 2**10:
        print(L)
        break


#23195
for N in range(1,100000):
    L = 172
    i = ceil(log2(N))
    I = ceil(L * i/ 8)
    if 356984 * I>= 54*2**20:
        print(N)
        break

