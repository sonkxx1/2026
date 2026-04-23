from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot,d) for d in cluster)
        res.append([sum_dist,dot])
    return min(res)[1]

with open(r'.\files\27_B_28766.txt') as file:
    dots =[]
    stars =[]
    for i in file:
        x,y,data = i.replace(',','.').split()
        dots.append(list(map(float,[x,y])))
        if data[0] == 'Z' and data[2:] == 'I':
            stars.append(list(map(float,[x,y])))



cluster_1 =[dot for dot in dots if dot[1]>23]
cluster_2 =[dot for dot in dots if 16<dot[1]<23]
cluster_3 =[dot for dot in dots if dot[1]<16]


s_cluster_1=[dot for dot in stars if dot[1]>23]
s_cluster_2 =[dot for dot in stars if 16<dot[1]<23]
s_cluster_3 =[dot for dot in stars if dot[1]<16]

center_2 = center(cluster_2)
center_3 = center(cluster_3)

B2 = dist(center_2,center_3)

B1=[]
for s in s_cluster_1:
    for y in s_cluster_1:
        if s!=y:
            B1.append(dist(s,y))

for s in s_cluster_3:
    for y in s_cluster_3:
        if s!=y:
            B1.append(dist(s,y))

from itertools import combinations
from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'.\files\27_B_28766.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'Z' and data[2:] == 'I':
            stars.append(list(map(float, [x, y])))

cluster_1 = [
    [d for d in dots if 23 < d[1]],
    [d for d in stars if 23 < d[1]]
]

cluster_2 = [
    [d for d in dots if 16 < d[1] < 23],
    [d for d in stars if 16 < d[1] < 23]
]

cluster_3 = [
    [d for d in dots if d[1] < 16],
    [d for d in stars if d[1] < 16]
]

clusters = [cluster_1, cluster_2, cluster_3]

dists = []
for cluster in clusters:
    dists += [dist(d1, d2) for d1, d2 in combinations(cluster[1], 2)]
B1 = min(dists)

max_cluster = center(max(clusters, key=lambda x: len(x[1]))[0])
min_cluster = center(min(clusters, key=lambda x: len(x[1]))[0])
B2 = dist(max_cluster, min_cluster)

print(B1 * 10_000, B2 * 10_000)


print(min(B1)*10000,B2*10000)






