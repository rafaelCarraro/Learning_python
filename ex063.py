#criar uma sequencia de fibonacci, com 'n' caracteres
print('\033[1m-'*22)
print('SEQUÊNCIA DE FIBONACCI')
print('-'*22, '\033[m')
t = int(input('Quantos termos deseja mostrar: '))
n = int(input('Qual será o primeiro número da sequência: '))
np = n + n
na = 0
print('{}, {}'.format(n, np), end=', ')
while t > 2:
    na = n + np
    t -= 1
    n = np
    np = na
    print(na, end='')
    print(', 'if 2 < t else '|', end='')
print(' FIMM')