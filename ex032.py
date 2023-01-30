a = int(input('Digite um ano? '))
if a % 100 == 0:
    if a % 400 == 0:
        print('Ano Bissexto')
    else:
        print('Não é Bissexto')
else:
    if a % 4 == 0:
        print('Ano Bissexto')
    else:
        print('Não é Bissexto')
#if a % 4 == 0 and a % 100 != 0 or a % 400 == 0: