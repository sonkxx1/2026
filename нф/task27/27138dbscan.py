from math import dist

with open(r'.\files\27A_27138.txt') as file:
    dots =[list(map(float, i.replace(',','.').split())) for i in file]

def center(cluster):
    res =[]
    for dot in cluster:
        sum_dist = sum(dist(dot,d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

eps = 1.3
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

print(abs(centers[0][0]-centers[1][0])*10000)
print(abs(centers[0][1]-centers[1][1])*10000)

with open(r'.\files\27B_27138.txt') as file:
    dots =[list(map(float, i.replace(',','.').split())) for i in file]

eps = 1.3
clusters=[]
while dots:
    cluster=[dots.pop()]
    for dot in cluster:
        for d in dots.copy():
            if dist(dot,d) < eps:
                cluster.append(d)
                dots.remove(d)
    clusters.append(cluster)

print([len(cluster) for cluster in clusters])
centers = [center(cluster) for cluster in clusters]


