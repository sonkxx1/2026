from math import dist

def center(cluster):
    res =[]
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'.\files\27_A_17915.txt') as file:
    dots =[list(map(float,i.replace(',','.').split())) for i in file]

cluster1 = [dot for dot in dots if dot[0] < 6]
cluster2 = [dot for dot in dots if dot[0] >8 and dot[1] >23]
cluster3 = [dot for dot in dots if dot[1] < 22 and dot[0] > 12]

center1 = center(cluster1)
center2 = center(cluster2)
center3 = center(cluster3)

print((center1[0] +center2[0]+center3[0])/3 *10000)
print((center1[1] +center2[1]+center3[1])/3 *10000)