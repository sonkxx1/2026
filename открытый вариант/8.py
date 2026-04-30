from itertools import product

alph = sorted('апрель')

for pos, val in enumerate(product(alph, repeat = 6), start = 1):
    val =''.join(val)
    if pos%2 != 0 and val[0] != 'а' and val[0] != 'л' and val.count('п') >= 2:
        print(pos,val)

#7903