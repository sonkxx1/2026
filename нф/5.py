ans =[]
for N in range(8,100000):
    R = f'{N:o}'
    if N % 2 == 0:
        R = R + R[-1]
    if N%2 != 0:
        R = R[-1] + R[1:-1]+ R[0]
    R = int(R,8)
    if R <254:
        ans.append(R)
print(max(ans))


