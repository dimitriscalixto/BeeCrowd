while True:
    try:
        w = input()
        cont = 0
        cont1 = 0
        menor = 0
        par = 0
        imp = 0
        for i in range(len(w)):
            if w[i] == "(":
                cont += 1
                menor += 1
                par += 1
            if w[i] == ")" and menor > 0:
                cont1 += 1
                menor -= 1
            if w[i] == ")":
                imp += 1
        if cont1 == par and cont1 == imp and par == imp:
            print('correct')
        else:
            print('incorrect')
    except EOFError:
        break