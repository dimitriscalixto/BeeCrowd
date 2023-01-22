arr = []
arr2 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P']
arr3 = ['ABCDEFGHIJKLMNOP']
contador = 0
contador1 = 0
contador2 = 0
for i in range(8):
    a,b = input().split()
    a = int(a)
    b = int(b)
    if a > b:
        arr2.remove(arr2[contador+1])
    else:
        arr2.remove(arr2[contador])
    contador += 1
for i in range(4):
    a, b = input().split()
    a = int(a)
    b = int(b)
    if a > b:
        arr2.remove(arr2[contador1+1])
    else:
        arr2.remove(arr2[contador1])
    contador1 += 1
for i in range(2):
    a,b = input().split()
    a = int(a)
    b = int(b)
    if a > b:
        arr2.remove(arr2[contador2+1])
    else:
        arr2.remove(arr2[contador2])
    contador2 += 1
a, b = input().split()
a = int(a)
b = int(b)
if a > b:
    print(arr2[0])
else:
    print(arr2[1])





