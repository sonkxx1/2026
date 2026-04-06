from functools import lru_cache
def F(n):
    return G(n-2)

@lru_cache(None)
def G(n):
    if n<100: return n
    return F(n-3) +1

for i in range(100,5001):
    G(i)

print(F(5000))