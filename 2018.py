while True:
    try:
        modalidade = input()
        posicoes = {}
        contador = 1
        for i in range(3):
            pais = input().split(' ')
            for j in range(len(pais)):
                if j == 0:
                    posicoes[pais[j]] = {'primeiro': +1}
                elif j == 1:
                    posicoes[pais[j]] = {'segundo': +1}
                elif j == 2:
                    posicoes[pais[j]] = {'terceiro': +1}
                contador += 1
        print(posicoes)
    except EOFError:
        break