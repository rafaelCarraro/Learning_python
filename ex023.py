'''n = int(input('Digite um número de até 4 digitos: '))
ns = str(n + 10000)
print('o número {} possui {} milhar'.format(n, n[1]))
print('o número {} possui {} centenas'.format(n, n[2]))
print('o número {} possui {} dezenas'.format(n, n[3]))
print('o número {} possui {} unidades'.format(n, n[4]))'''
n = int(input('Insira um número: '))
m = n / 1000
c = (n / 100) % 10
d = (n / 10) % 10
u = n % 10
print('o número {} possui {:.0f} milhar'.format(n, m))
print('o número {} possui {:.0f} centenas'.format(n, c))
print('o número {} possui {:.0f} dezenas'.format(n, d))
print('o número {} possui {:.0f} unidades'.format(n, u))
