
with open(r'.\files\17_11236.txt') as file:
    data = [int(i) for i in file]

maxx = max(i for i in data if 1000<= abs(i)<= 9999 and abs(i) %10 == 0 )
min_2 = min(i for i in data if 10<=abs(i)<= 99 ) **2

ans =[]
for num1,num2,num3 in zip(data,data[1:], data[2:]):
    u1 =sum( i > min_2 for i in (num1,num2,num3)  )
    u2 = ((abs(num1) * abs(num2) *abs(num3)) % abs(maxx) == 0)
    if u1 and u2:
        ans.append(abs(sum(num1+num2+num3)))
print(len(ans), max(ans))