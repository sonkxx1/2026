from fnmatch import fnmatch

for i in range(1917, 10 ** 10 + 1,1917):
    if fnmatch(str(i), '3?12?14*5'):
        print(i, i// 1917)
############################################
from itertools import product

ans = []
for V1 in range(0,10):
    for V2 in range(0,10):
        for l in range(0, 3):
            for Z in product('0123456789', repeat = l):
                Z = ''.join(Z)
                num = int(f'3{V1}12{V2}14{Z}5')
                if num % 1917 == 0 and num <= 10**10:
                    ans.append([num, num//1917])

for i in sorted(ans):
    print(*i)

