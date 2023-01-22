n = int(input())
for i in range(n):
    d = input()
    cont = 0
    cont1 = 0
    total = 0
    for j in range(len(d)):
        if d[j] == '<':
            cont += 1
        if d[j] == '>' and cont > 0:
            total += 1
            cont -= 1
    print(total)


