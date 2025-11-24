def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

num = 729**8 - 3**18 +85

print(convert(num,9).count('0'))