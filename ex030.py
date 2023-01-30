n = int(input('Digite um número: '))
'''if (n % 2) == 0:
    print('Você digitou {}, este número é par'.format(n))
else:
    print('Voce digitou {}, este número é impar'.format(n))'''
print('Você digitou {}, este número é {}'.format(n, '\033[33mPar' if n%2 == 0 else '\033[32mImpar'))
