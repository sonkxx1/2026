with open(r'.\files\task-9.txt') as file:
    data = [list(map(int, i.split())) for i in file]

ans = []
for pos, line in enumerate(data, start=1):
    u = [line.count(i) for i in set(line)]
    if sorted(u) == [1, 1, 1, 1, 2]:
        pov = [n for n in set(line) if line.count(n) != 1]
        ne_pov = [n for n in set(line) if line.count(n) == 1]
        if pov[0] >= sum(ne_pov) / len(ne_pov):
            print(pos)
            break
