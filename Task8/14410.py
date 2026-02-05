from itertools import product

alph = sorted('СОЛНЦЕ')

for pos, val in enumerate(product(alph,repeat =6),start = 1):
    val =''.join(val)
    if val.count('Ц') == 2 and pos%2 ==2 and val[0] not in 'ОЕ':
        print(pos)

