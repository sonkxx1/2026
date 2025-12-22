from itertools import product

alph = sorted('гранит')

ans = []
for pos,val in enumerate(product(alph,repeat = 6), start = 1):
    if pos % 2 != 0 and val.count('а') == 1 and val[0] != 'а' and val[0] != 'и' and val[0] != 'г':
        ans.append(pos)
print(min(ans))

