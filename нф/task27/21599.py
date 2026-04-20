from math import dist


def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]


with open(r'.\files\27_A_21599.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

cluster_A_1 =[dot for dot in dots if dot[1] <-7]
cluster_A_2 =[dot for dot in dots if -7<dot[1]<11/14 *dot[0] -11]
cluster_A_3 =[dot for dot in dots if dot[1]>11/14 *dot[0] -11]

center_A_1 = center(cluster_A_1)
center_A_2 = center(cluster_A_2)
center_A_3 = center(cluster_A_3)

print((center_A_1[0]+center_A_2[0]+center_A_3[0])/3*10000)
print((center_A_1[1]+center_A_2[1]+center_A_3[1])/3*10000)

with open(r'.\files\27_B_21599.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]
    
cluster_B_1 =[dot for dot in dots if dot[1] <-5]
cluster_B_2 =[dot for dot in dots if -5<dot[1]<dot[0]]
cluster_B_3 =[dot for dot in dots if 10/7*dot[0]+10>dot[1]>dot[0]]
cluster_B_4 =[dot for dot in dots if dot[1]>10/7*dot[0]+10 and dot[0]>-10]
cluster_B_5 =[dot for dot in dots if dot[0] <-10 and dot[1]> -2*dot[0]-26]
cluster_B_6 =[dot for dot in dots if dot[1] <-2*dot[0]-26]

center_B_1 = center(cluster_B_1)
center_B_2 = center(cluster_B_2)
center_B_3 = center(cluster_B_3)
center_B_4 = center(cluster_B_4)
center_B_5 = center(cluster_B_5)
center_B_6 = center(cluster_B_6)

print((center_B_1[0]+center_B_2[0]+center_B_3[0]+center_B_4[0]+center_B_5[0]+center_B_6[0])/6*10000)
print((center_B_1[1]+center_B_2[1]+center_B_3[1]+center_B_4[1]+center_B_5[1]+center_B_6[1])/6*10000)








