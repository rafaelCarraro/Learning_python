n = (int(input('Digite um núemro: ')), int(input('Digite um núemro: ')), int(input('Digite um núemro: ')), int(input('Digite um núemro: ')))
print('-'*25)
print(f'O número nove apareceu {n.count(9)} vezes;')
if 3 in n:
    print(f'O número 3 foi o {n.index(3)+1}º número a ser digitado')
else:
    print('O valor 3 não foi digitado nenhuma vez')
print('O núemros pares foram:', end=' ')
for c in n:
    if c % 2 == 0:
        print(c, end=' ')
print('\n', '-'*25)