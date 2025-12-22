from itertools import product

alph = sorted('мизантроп')

for pos, val in enumerate(product(alph, repeat = 5), start = 1):
    val = ''.join(val)
    if pos % 2 ==0 and val[0] == 'н' and val.count('р') == 2:
        print(pos)