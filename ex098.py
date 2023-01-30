from time import sleep


def cont(a, b, c):
    """
    -> Print a gradual count from given parameters
    :param a: the begining of the count
    :param b: the end of the count
    :param c: the pace of the count
    :return: no return
    made by a communist nobody
    """
    if c == 0:
        c += 1
    print('-=' * 30)
    print('A sequencia é', end=' ')
    if a < b:
        for x in range(a, b + 1, c):
            print(f'{x}', end='->')
            sleep(0.3)
        print('FIMM!!')
    elif a > b:
        for y in range(a, b - 1, c * -1):
            print(f'{y}', end='->')
            sleep(0.3)
        print('FIMM!!')


cont(1, 10, 1)
cont(10, 0, 2)
cont(int(input('Digite o início: ')),
     int(input('Digite o fim: ')),
     int(input('Digite o passo: ')))
help(cont)