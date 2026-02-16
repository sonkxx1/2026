from functools import lru_cache



@lru_cache(None)
def F(n):
    if n>30: return F(n-6) +2048
    return 3 * (G(n-5) + 13)

@lru_cache(None)
def G(n):
    if n >= 22337: return 2 * n +50
    return G(n+11) - 48

for i in range(22337,1,-1):
    G(i)

print(F(5078))