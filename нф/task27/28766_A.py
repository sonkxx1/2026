from math import dist

with open(r'.\files\27_A_28766.txt') as file:
    dots =[]
    stars =[]
    for i in file:
        x,y,data = i.replace(',','.').split()
        dots.append(list(map(float,[x,y])))
        if data[0] == 'Y' and data[2:] == 'III':
            stars.append(list(map(float,[x,y])))

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot,d) for d in cluster)
        res.append([sum_dist,dot])
    return min(res)[1]

cluster_1 = [dot for dot in dots if dot[1]<8]
cluster_2 = [dot for dot in dots if dot[1]>8]

center_1  = center(cluster_1)
center_2  = center(cluster_2)

clusters =[cluster_1,cluster_2]

min_cluster = center( min(clusters,key=len))

dists =[]
for i in stars:
    dists.append(dist(min_cluster,i))

print(min(dists)*10000)
print(max(dists)*10000)
