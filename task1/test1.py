from itertools import permutations

graph = 'HD DA AC BC HB HF FE EG GC GA'.split()
matrix = '258 17 56 68 138 347 26 145'.split()

print(*range(1,9))
for i in permutations('ABCDEFGH'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)


