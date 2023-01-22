n = int(input())

for i in range(n):
    p = int(input())
    lista = [int(x) for x in input().split()]
    ord = sorted(lista)
    ord.reverse()
    cont = 0
    for j in range(len(lista)):
        if lista[j] == ord[j]:
            cont += 1
    print(cont)