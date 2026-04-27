from math import dist
from itertools import combinations

with open(r'.\files\27_B_29081.txt') as file:
    dots= []
    stars=[]
    for i in file:
        x, y, data = i.replace(',','.').split()
        dots.append(list(map(float,[x,y])))
        if data[1] in '89':
            stars.append(dots[-1])

stars_1 =[dot for dot in stars if 22<dot[1]]
stars_2 =[dot for dot in stars if 22>dot[1]>16]
stars_3 =[dot for dot in stars if 16>dot[1]]

dists=[]
for s1 in stars_1:
    for s2 in stars_2:
        for s3 in stars_3:
            dists.append(dist(s1,s2))
for s1 in stars_1:
    for s2 in stars_2:
        for s3 in stars_3:
            dists.append(dist(s1,s3))
for s1 in stars_1:
    for s2 in stars_2:
        for s3 in stars_3:
            dists.append(dist(s3,s2))

print(min(dists)*10000)

dists =[]
for s1 in stars_1:
    for s2 in stars_1:
        if s1 != s2:
            dists.append(dist(s1,s2))
for s1 in stars_2:
    for s2 in stars_2:
        if s1 != s2:
            dists.append(dist(s1,s2))
for s1 in stars_3:
    for s2 in stars_3:
        if s1 != s2:
            dists.append(dist(s1,s2))

B2= sum(dists)/len(dists)

print(B2*10000)

print("#########################")

stars_1 =[dot for dot in stars if 22<dot[1]]
stars_2 =[dot for dot in stars if 22>dot[1]>16]
stars_3 =[dot for dot in stars if 16>dot[1]]
all_stars =[stars_1,stars_2,stars_3]

B1=min(dist(s1,s2) for cl1,cl2 in combinations(all_stars,2) for s1 in cl1 for s2 in cl2)
B2=[dist(s1,s2) for cl in all_stars for s1,s2 in combinations(cl,2)]
B2=sum(B2)/len(B2)

print(B1*10000)
print(B2*10000)

#####################


cluster_1 = [s for s in dots if 22 < s[1]]
cluster_2 = [s for s in dots if 16 < s[1] < 22]
cluster_3 = [s for s in dots if s[1] < 16]
clusters = [cluster_1, cluster_2, cluster_3]

B1 = []
B2 = []
for s1, s2 in combinations(stars, 2):
    u = any(s1 in cl and s2 in cl for cl in clusters)
    d = dist(s1, s2)
    if u: B2.append(d)
    else:B1.append(d)

print(min(B1) * 10_000, sum(B2) / len(B2) * 10_000)




