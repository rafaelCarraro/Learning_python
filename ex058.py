from random import randint
from time import sleep

print('Vamos jogar um joguinho, eu pensei em um número de 0 a 5')
nc = randint(0, 10)
nu = 11
c = 0
while nc != nu:
    nu = int(input('Tente adivinhar qual: '))
    nc = randint(0, 10)
    print('\033[33mPROCESSANDO...\033[m')
    sleep(0.2)
    print('O número que eu pensei foi {}{}{}'.format('\033[33m', nc, '\033[m'))
    c += 1
    if nu != nc:
        print('\033[31mERRRRRROOOOUUUUU\033[m')

print('\033[32mVoce acertou carai!! Só precisou de {} rodadas'.format(c))
