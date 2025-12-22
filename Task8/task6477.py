from itertools import permutations

cnt = 0
for val in set(permutations('левиоса')):
    val = ''.join(val)
    if val[0] not in 'еиоа' and val[len(val)//2] not in 'лвс':
        cnt += 1

print(cnt)