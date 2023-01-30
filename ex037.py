#conversao para bases numericas
n = int(input('Digite um número intero '))
r = int(input(('Escolha para qual base você deseja converter o número\n1 para Binário;\n2 para Octal;\n3 para Hexadecimal\n Resposta: ')))
if r == 1:
    print('Aqui esta seu número em binário {}'.format(bin(n)))
elif r == 2:
    print('Aqui está o seu número em octal {}'.format(oct(n)))
elif r == 3:
    print('Aqui esta o seu número em Hexadecimal {}'.format(hex(n)))
