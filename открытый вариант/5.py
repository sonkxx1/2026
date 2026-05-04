ans =[]
for N in range(1,1000):
    R = f'{N:b}'
    if R.count('1')% 2 ==0:
        R = R+'0'
        R = '10'+ R[2:]
    else:
        R = R + '1'
        R = '11' + R[2:]
    R =int(R,2)
    if R<=19:
        ans.append(N)

print(max(ans))



