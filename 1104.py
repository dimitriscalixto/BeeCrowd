while True:
    a1, b1 = input().split()
    a1 = int(a1)
    b1 = int(b1)
    if a1 == b1 == '0':
        break
    fa = [int(x) for x in input().split()]
    fb = [int(x) for x in input().split()]
    a = set(fa)
    b = set(fb)
    c = b
    if len(a) < len(b):
        dif = a - b
        print(len(dif))
    else:
        print(len(c-a))