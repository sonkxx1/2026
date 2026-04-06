from sys import setrecursionlimit
def F(n):
    if n<=5: return 1
    return n + F(n-2)

setrecursionlimit(1500)#примерное колличиство шагов с шагом -2
print(F(2126) - F(2122))