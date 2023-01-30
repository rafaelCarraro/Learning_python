def ajuda(c):
    titulo(help(c))

def titulo(msg, cor):
    l = len(msg)
    print('\033[41m', '~' * l)
    print(msg)
    print('~' * l, '\033[m')



comando = ''
while True:
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)