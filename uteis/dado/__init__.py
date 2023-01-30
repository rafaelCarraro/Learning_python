def leiadin(n=''):
    n.replace(',', '.')
    while True:
        if not n.isnumeric():
            print(f'\033[1;31mERRO: {n} é um preço invalido!')
        else:
            return n
            break


def leiadi(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.')
        if entrada.isalpha() or entrada.strip() == '':
            print(f'\033[1;31mERRO: \"{entrada}\" é um preço invalido!\033[m')
        else:
            valido = True
            return float(entrada)
