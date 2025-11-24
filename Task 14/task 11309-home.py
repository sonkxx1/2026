from string import printable as alph

for x in alph[:27]:
    num1 = int(f'8{x}38{x}68',27)
    num2 = int(f'37{x}3163', 27)
    num = num1 + num2
    if num % 26 == 0:
        print(x, num //26)