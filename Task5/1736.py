ans =[]

for N in range(1, 100000):
    R=bin(N)[2:]
    R = R.replace('0','00').replace('1','11')
    if int(R,2) > 63:
        ans.append(int(R,2))
print(min(ans))
