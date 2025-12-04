from itertools import*

cnt=0
for val in product('гепард',repeat = 5):
    val =''.join(val)
    if val[0] !='а' and val[-1] != 'е' and val.count('г') == 1:
        cnt +=1
print(cnt)