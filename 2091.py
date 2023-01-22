while True:
    n = int(input())
    if n == 0:
        break
    num = input().split()
    for i in range(0,len(num)):
        m = num[0]
        num.remove(num[0])
        if m in num:
            num.remove(m)
        else:
            print(m)
            break