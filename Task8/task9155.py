from itertools import *

alph = sorted ('апрель', reverse = True)
cnt = 0
for pos, val in enumerate(product(alph, repeat = 5), start =1):
    val =''.join(val)
    if val[-1] == 'ь' and pos <= 387:
        cnt += 1

print(cnt)