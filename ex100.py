from random import randint
from time import sleep


def sorteio(lis):
    """Choose ramdomly nombers and add them to a list
     :param lis: is a list where the numbers are added.
     :return: no return"""
    print('Sorteando os valores da lista!', end=' ')
    for x in range(0, 5):
        n = randint(1, 10)
        lis.append(n)
        print(f'{n}', end='->')
        sleep(0.4)
    print('PRONTO!')


def sump(lis):
    """From a list, select and sum all even numbers
    :param lis: is a list
    :return: no return"""
    s = 0
    print(f'Somando os valores pares em {lis}', end=', ')
    for i in lis:
        if i % 2 == 0:
            s += i
    print(f'temos {s}')


numeros = []
sorteio(numeros)
sump(numeros)
help(sorteio)