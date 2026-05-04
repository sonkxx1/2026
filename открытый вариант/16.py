from sys import setrecursionlimit
def f(n):
    if n<10: return 1
    return (n+3) * f(n-3)
setrecursionlimit(10**6)
print((f(247563)//519-477*f(247560))//f(247557))

