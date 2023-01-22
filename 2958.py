n,m = input().split()
n = int(n)
listav = []
listad = []
for i in range(n):
    line = input().split()
    for j in range(len(line)):
        if 'V' in line[j]:
            listav.append(line[j])
        if 'D' in line[j]:
            listad.append(line[j])
    listav.sort(reverse=True)
    listad.sort(reverse=True)
for j in range(len(listav)):
    print(f'{listav[j][0]}V')
for k in range(len(listad)):
    print(f'{listad[k][0]}D')

