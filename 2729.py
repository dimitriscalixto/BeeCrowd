n, times = input().split()
vet = []
aux = []
cont = 0
cont2 = 0
for i in range(int(n)):
    a,b = input().split()
    hab = int(b)
    vet.append([a,hab])
    aux2 = [a,hab]
vet.sort(key=lambda x: x[1],reverse=True)
for i in range(int(times)):
    aux.append([])
for aux2 in vet:
    x = cont%int(times)
    aux[x].insert(0,aux2[0])
    cont += 1
for i in aux:
    cont2 += 1
    i.sort()
    print(f'Time {cont2}')
    aux3 = " "
    for j in i:
        aux3 += str(j) + "\n"
    print(f'{aux3[:-1]}\n')