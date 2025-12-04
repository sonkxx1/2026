from itertools import *

alph = sorted('пскаль')
cnt = 0

for val in product(alph, repeat =4):
    val =''.join(val)
    if val[0] != 'ь' and 'ьь'not in val:
        cnt += 1

print(cnt)