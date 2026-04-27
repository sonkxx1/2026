from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot,d) for d in cluster)
        res.append([sum_dist,dot])
    return min(res)[1]


with open(r'.\files\27_B_29080.txt') as file:
    dots= []
    stars=[]
    for i in file:
        x, y, data = i.replace(',','.').split()
        dots.append(list(map(float,[x,y])))
        if data[0] == 'L':
            stars.append(dots[-1])


cluster_1 =[dot for dot in dots if 22<dot[1]]
cluster_2 =[dot for dot in dots if 22>dot[1]>16]
cluster_3 =[dot for dot in dots if 16>dot[1]]


stars_1 =[dot for dot in stars if 22<dot[1]]
stars_2 =[dot for dot in stars if 22>dot[1]>16]
stars_3 =[dot for dot in stars if 16>dot[1]]
stars =[stars_1,stars_2,stars_3]
print(len(stars_1))
print(len(stars_2))
print(len(stars_3))

center_1= center(cluster_1)
center_2= center(cluster_2)
center_3= center(cluster_3)
centers =[center_1,center_2,center_3]

print(dist(center_1,center_3)*10000)





dists=[]
for s1 in stars_1:
    for s2 in stars_2:
        dists.append(dist(s1,s2))
for s1 in stars_1:
    for s3 in stars_3:
        dists.append(dist(s1,s3))
for s2 in stars_2:
    for s3 in stars_3:
        dists.append(dist(s3,s2))
print(max(dists)*10000)


