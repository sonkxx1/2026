def f(num):
    d = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            d|= {i, num // i}

    if d:
        M= sum(d)//len(d)
        if M%1000 == 313 and str(M)[-3:]:
            return M
    return 0


cnt = 0
for N in range (1,700000)[::-1]:
    if M := f(N):
        print(N,M)
        cnt += 1
        if cnt == 7:
            break