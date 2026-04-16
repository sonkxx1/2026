from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot,d) for d in cluster)
        res.append([sum_dist,dot])
    return min(res)[1]


with open (r'.\files\27_A_23209.txt') as file:
    dots = [list(map(float,i.replace(',','.').split())) for i in file]

eps = 1
clusters = []
while dots:
    cluster =[dots.pop()]
    for dot in cluster:
        for d in dots.copy():
            if dist(dot,d) < eps:
                cluster.append(d)
                dots.remove(d)
    clusters.append(cluster)

print([len(cluster) for cluster in clusters])
centers = [center(cluster) for cluster in clusters]


print(max(centers[0][0],centers[1][0])*10000)
print(max(centers[0][1],centers[1][1])*10000)

with open (r'.\files\27_B_23209.txt') as file:
    dots = [list(map(float,i.replace(',','.').split())) for i in file]
print('\\\\\\\\\\\\')
eps = 1
clusters = []
while dots:
    cluster =[dots.pop()]
    for dot in cluster:
        for d in dots.copy():
            if dist(dot,d) < eps:
                cluster.append(d)
                dots.remove(d)
    if len(cluster) >4:
        clusters.append(cluster)

print([len(cluster) for cluster in clusters])
centers = [[len(cluster),center(cluster)] for cluster in clusters]

max_cluster_B= max(centers)
min_cluster_B= min(centers)

print((max_cluster_B[1][0]-min_cluster_B[1][0])*10000)
print((max_cluster_B[1][1]-min_cluster_B[1][1])*10000)





