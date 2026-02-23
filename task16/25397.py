from functools import lru_cache

@lru_cache(None)
def F(n):
    if n>40: return F(n-4)
    return 3 * (G(n-2) -15 )

@lru_cache(None)
def  G(n):
    if n>=301298: return 10* n +50
    return G(n+7) - 21

for i in range(301298, 1,-1):
    G(i)
print(F(2026))


