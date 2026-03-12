with open(r'.\files\17_4597.txt') as file:
    data = [int(i) for i in file]

minn = min(data)

ans = []
for i in range(len(data)):
    num1, num2 = data[i:i + 2]
    u1 = num1 % 117 == minn
    u2 = num1 % 117 == minn
    if any([u1, u2]) and u1 + u2>=1:
        ans.append(num1+num2)


print(len(ans),max(ans))
