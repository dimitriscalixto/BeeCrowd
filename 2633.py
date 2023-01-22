while True:
    try:
        n = int(input())
        churras = {}
        lista = []
        for i in range(n):
            peca,idade = input().split()
            churras[peca] = int(idade)
        for item in sorted(churras, key=churras.get):
            lista.append(item)

        print(' '.join(lista))
    except EOFError:
        break

