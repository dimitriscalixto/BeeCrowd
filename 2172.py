while True:
    bonus, exp = input().split(" ")
    if bonus and exp == '0':
        break
    else:
        print(int(bonus) * int(exp))