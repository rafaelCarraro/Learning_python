from time import sleep


def maior(*num):
    cont = maior = 0
    print('-=' * 35)
    print('Analisando os valores passados...')
    for x in num:
        print(f'{x}', end=' ')
        sleep(0.2)
        if cont == 0:
            maior = x
        else:
            if x > maior:
                maior = x
        cont +=1
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


maior(2, 6, 6, 5, 9, 8, 7, 1, 25, 2)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
