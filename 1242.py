while True:
    try:
        fita = str(input())
        pc = ['BS','SB','CF','FC']
        a = ['B','S','C','F']
        total = 0
        fita2 = list(fita)
        resto = ''
        for i in a:
            if i in fita2:
                resto += i
        print(resto)
    except EOFError:
        break