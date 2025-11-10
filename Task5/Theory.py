# Системы счисления

# Двоичная система
N = 25
# bin() - переводит десятичное число в двоичную систему.
# Принимает на вход int, возвращает str.
# [2:] - срез, убирающий первые два символа '0b'
print(bin(N)[2:])
# f'' - форматируемая строка,
# которая позволяет вставлять в себя переменные
print(f'{N:b}')

# Восьмеричная система
print(oct(N)[2:])
print(f'{N:o}')

# Шестнадцатеричная система
print(hex(N)[2:])
print(f'{N:x}')

# Перевод в любую систему счисления (2 <= sys <= 9)
def convert(num, sys):
    res = ''
    while num != 0:
        res += str(num % sys)
        num //= sys
    return res[::-1]

# Перевод в любую систему счисления (2 <= sys <= 36)
from string import printable

def convert2(num, sys):
    res = ''
    while num != 0:
        res += printable[num % sys]
        num //= sys
    return res[::-1]

#Срезы
test='hello world'
#Извлечение первых двух символов
print(test[:2])
# Строка без первых двух символов
print(test[2:])
#Извлечение последних двух символов
print(test[-2:])
# Строка без последних двух символов
print(test[:-2])









