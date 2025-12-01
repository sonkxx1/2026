from itertools import *

# product - возвращает все возможные расстановки символов длины repeat
alph_1 = 'ab'
for val in product(alph_1, repeat=2):
    val = ''.join(val)
    print(val)

#permutations -возвращает все возможные перестановки символов
alph_2 = 'ab'
for val in permutations(alph_2):
    val = ''.join(val)
    print(val)
# enumerate
alph_3 = 'abch'
res = enumerate(alph_3, start=1)
print(*res)
