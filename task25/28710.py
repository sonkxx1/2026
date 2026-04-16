def fact(num):
    d = []
    while num % 2 == 0:
        d += [2]
        num //= 2
    i = 3
    while i * i < num +1:
        while num % i == 0:
            d += [i]
            num //= i
        i += 2
    if num > 1:
        d += [num]
    return d

def f(num):
    d = set()
    for i in range(1, int(num ** .5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    if len(d) % 90 == 0:
        return True
    return False

cnt = 0
for N in range(3_600_000+1,10**30):
    d = fact(N)
    if len(d) == 3:
        if all('3' in N and '5' in N for N in map(str, d)):
            cnt += 1
        print(N,max(d))
        cnt += 1
        if cnt == 5:
            break