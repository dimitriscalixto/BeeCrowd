par = input()
cont = 0
menor = 0
total = 0
cont1 = 0
for l in par:
    if l == '(':
        cont += 1
    elif l == ')' and cont > 0:
        cont -= 1
if cont:
    print(f'Ainda temos {cont} assunto(s) pendente(s)!')
else:
    print('Partiu RU!')