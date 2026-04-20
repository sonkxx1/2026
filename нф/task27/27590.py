from math import dist

def anticenter(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot,d) for d in cluster)
        res.append([sum_dist,dot])
    return max(res)[1]

with open(r'.\files\27A_27590.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

cluster_A_1 = [dot for dot in dots if dot[1] <10]
cluster_A_2 = [dot for dot in dots if dot[1] >10]

center_A_1 = anticenter(cluster_A_1)
center_A_2 = anticenter(cluster_A_2)

print(len(cluster_A_1))
print(len(cluster_A_2))
print((center_A_2[0]+center_A_2[1] )*10000)
print((center_A_1[0]+center_A_1[1] )*10000)

with open (r'.\files\27B_27590.txt') as file:
    dots = [list(map(float,i.replace(',','.').split())) for i in file]

cluster_B_1 = [dot for dot in dots if 10<dot[1]<20]
cluster_B_2 =[dot for dot in dots if 13<dot[0]<17 and dot[1]>20]
cluster_B_3= [dot for dot in dots if 20<dot[0]<24]

center_B_1 = anticenter(cluster_B_1)
center_B_2 = anticenter(cluster_B_2)
center_B_3 = anticenter(cluster_B_3)

print(len(cluster_B_1))
print(len(cluster_B_2))
print(len(cluster_B_3))
print((cluster_B_3[0])*10_000)
print((cluster_B_1[1])*10_000)