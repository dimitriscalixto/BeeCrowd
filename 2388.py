n = int(input())
total = 0
for i in range(n):
    t,v = input().split()
    total = total + int(t)*int(v)
print(total)