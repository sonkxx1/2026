from string import printable


def convert(num,sys):
    res = ''
    while num:
        res += printable[num%sys]
        num //= sys
    return res[::-1]


R = 283**382 + 9**15 + 2**3
new_R = convert(R ,14)

print(abs)



