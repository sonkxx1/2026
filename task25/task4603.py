from fnmatch import fnmatch

for N in range(141, 10 ** 8):
    if fnmatch(str(N), '1234*7'):
        print(N, N// 141)