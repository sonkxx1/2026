from itertools import product
from string import printable

cnt = 0
for val in product(printable[:12], repeat = 7):
    val=''.join(val)
    if val[0] != '0':
        for i in '0369':
            val = val.replace(i,'*')
        for i in '124578ab'
            val = val.replace(i, '+')
        if '**' not in val