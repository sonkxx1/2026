def f(num):
    d = set()
    for i in range (2, int(num ** .5) +1):
        if num % i == 0:
            d |= {i, num // i}
    if len(d) == 3:
        return max(d)
    return 0

for N in range(int(106732567 **.5),int( 152673836 ** .5)):
    if M := f(N*N):
        print(N*N,M)