from itertools import product

alph = sorted('аексн')

for pos, val in enumerate(product(alph , repeat =6),start = 1):
    val = ''.join(val)
    if 'сенека' in val:
        print(pos)