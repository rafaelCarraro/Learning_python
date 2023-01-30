o = 0
r = 0
x = ''
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
while o != 7:
    o = int(input('''Qual opção deseja realizar:
               [1] SOMAR
               [2] DIMINUIR
               [3] MULTIPLICAR
               [4] DIVIDIR
               [5] MAIOR e MENOR
               [6] DIGITAR NOVOS NUMEROS
               [7] SAIR DO PROGRAMA.'''))
    if o <= 4:
        if o == 1:
            r = n1 + n2
            x = 'Soma'
        elif o == 2:
            r = n1 - n2
            x = 'subtração'
        elif o == 3:
            r = n1 * n2
            x = 'multiplicação'
        elif o == 4:
            r = n1 / n2
            x = 'divisão'
        print('--' * 15)
        print('O resultado da {} entre {} e {} é de {:.2f}'. format(x, n1, n2, r))
        print('--' * 15)
    elif o == 5:
        if n1 > n2:
            r = n1
        elif n1 < n2:
            r = n2
        print('--' * 15)
        print('O maior número entre {} e {} é {}'.format(n1, n2, r))
        print('--' * 15)
    elif o == 6:
        print('Informe os números novamente:')
        n1 = int(input('Digite um novo número: '))
        n2 = int(input('Digite outro novo número: '))
    elif o == 7:
        print('--' * 15)
        print('Obrigado, e até logo')
        print('--' * 15)
        break
    else:
        print('--' * 15)
        print('Opção inválida, tente novamente')
        print('--' * 15)
print('FIM')
