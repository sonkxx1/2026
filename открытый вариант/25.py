from fnmatch import fnmatch

for i in range(9874,10**10,9874):
    if fnmatch(str(i),'89*6?7?9?'):
        print(i,i//9874)