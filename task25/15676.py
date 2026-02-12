from fnmatch import fnmatch
from itertools import product
def sost(num):
    for i in range(2, int( num ** .5) + 1):
        if num % i == 0:
            return True
    return False

sost_nums =[]
for N in range(4, 10000):
    if sost(N):
        sost_nums += [N]


for i in range(22768, 10**8 +1, 22768):
    for N in sost_nums:
        if fnmatch(str(i), f'1{N}03*6*'):
            print(i,N)

###################################
ans = []
for l1 in range(1, 5):
    for N in range(10 ** l1 -1, 10 ** l1):
        if sost(N):
            for l2 in range(0, 4-l1 +1):
                for Z1 in product('0123456789', repeat = l2):
                    Z1 =''.join(Z1)
                    for l3 in range(0, 4-l1-l2+1):
                        for Z2 in product('0123456789', repeat = l3):
                            Z2 =''.join(Z2)
                            num = int(f'1{N}03{Z1}6{Z2}')
                            if num % 22768 == 0 and num < 10**8:
                                ans.append([num,N])
for i in sorted (ans):
    print(*i)
