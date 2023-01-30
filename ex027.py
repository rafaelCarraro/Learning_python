n = str(input('Insira seu nome completo: ')).strip()
nd = n.split()
print('O seu nome é: {} \nSendo que seu primeiro nome é: {} \nJá o último nome é: {}'.format(n, nd[0], nd[len(nd)-1]))
