from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot,d) for d in cluster)
        res.append([sum_dist,dot])
    return min(res)[1]


with open(r'.\files\27_A_29080.txt') as file:
    dots= []
    stars=[]
    for i in file:
        x, y, data = i.replace(',','.').split()
        dots.append(list(map(float,[x,y])))
        if data[0] == 'L':
            if data[1] == '3':
                stars.append(dots[-1])

cluster_1 = [dot for dot in dots if dot[1]>8]
cluster_2 = [dot for dot in dots if dot[1]<8]

stars_1 = [dot for dot in stars if dot[1]>8]
stars_2 = [dot for dot in stars if dot[1]<8]

center_1 = center(cluster_1)
center_2 = center(cluster_2)

print(len(cluster_1))
print(len(cluster_2))

d=[]
for i in stars:
    d.append(dist(center_1, i))
m=[]
for i in stars:
    m.append(dist(center_2, i))

print(max(d)*10000,max(m)*10000)

