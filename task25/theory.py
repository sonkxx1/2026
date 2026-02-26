from fnmatch import fnmatch

for i in range(1917, 10 ** 10 + 1,1917):
    if fnmatch(str(i), '3?12?14*5'):
        print(i, i// 1917)
############################################
from itertools import product

ans = []
for V1 in range(0,10):
    for V2 in range(0,10):
        for l in range(0, 3):
            for Z in product('0123456789', repeat = l):
                Z = ''.join(Z)
                num = int(f'3{V1}12{V2}14{Z}5')
                if num % 1917 == 0 and num <= 10**10:
                    ans.append([num, num//1917])

for i in sorted(ans):
    print(*i)



# Задачи с масками

# Библиотека для проверки строк под маску
from fnmatch import fnmatch

# ? - ровно один любой символ
# * - любое кол-во любых символов

print(fnmatch('', '*'))


# КомпЕГЭ 4603 (рекомендованное решение)
from fnmatch import fnmatch

for N in range(12347 - 12347 % 141, 10 ** 8 + 1, 141):
   if fnmatch(str(N), '1234*7'):
       print(N, N // 141)


#########################################
print('#################')

# КомпЕГЭ 4603 (решение перебором)
from itertools import product

for l in range(0, 4):
    for val in product('0123456789', repeat=l):
        val = '1234' + ''.join(val) + '7'
        if int(val) % 141 == 0:
            print(val, int(val) // 141)

# Проверка чисел на простоту
def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True

print(is_prime(1))

# Разложение числа на простые множители
def fact(num):
    d = []
    while num % 2 == 0:
        d += [2]
        num //= 2

    for i in range(3, int(num ** .5) + 1, 2):
        while num % i == 0:
            d += [i]
            num //= i

    if num > 2:
        d += [num]

    return d

# Разложение числа на простые множители (чуть быстрее)
def fact_3(num):
    d = []
    while num % 2 == 0:
        d += [2]
        num //= 2

    i = 3
    while i < int(num ** .5) + 1:
        while num % i == 0:
            d += [i]
            num //= i
        i += 2

    if num > 2:
        d += [num]

    return d


