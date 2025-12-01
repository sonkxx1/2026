from itertools import *

alph = sorted('мангуст')
for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if val[0] != 'у' and val.count('м') == 2 and val.count('г') <= 1:
        print(pos)
