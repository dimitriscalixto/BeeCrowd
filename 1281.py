n = int(input())
for i in range(n):
    feira = {}
    final = 0.0

    m = int(input())
    for j in range(m):
        item,preco = input().split()
        feira[item] = float(preco)
    p = int(input())
    for k in range(p):
        item, qt = input().split()
        final += feira[item] * int(qt)
    print(final)