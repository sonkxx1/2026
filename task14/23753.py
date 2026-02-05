from string import printable as alph
for x in alph[:29]:
    num1 = int(f'923{x}89957', 29)
    num2 = int(f'524{x}6152', 29)
    num = num1 + num2
    if num % 28 == 0:
        print(num // 28)