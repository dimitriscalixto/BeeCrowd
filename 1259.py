par = []
impar = []
n = int(input())
for i in range(n):
    num = int(input())
    p = 0
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
    par.sort()
    impar.sort(reverse=True)
for p in par:
    print(p)
for im in impar:
    print(im)
