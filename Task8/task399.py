from itertools import permutations

cnt = 0
for val in set(permutations('ворота', r = 6)):
    val= "".join(val)
    if 'оо' not in val and 'оа' not in val and 'ао' not in val:
        cnt += 1

print(cnt)

