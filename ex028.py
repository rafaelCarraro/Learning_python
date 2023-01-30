from random import randint
from time import sleep
print('Vamos jogar um joguinho, eu pensei em um número de 0 a 5')
nu = int(input('Tente adivinhar qual: '))
nc = randint(0,5)
print('\033[33mPROCESSANDO...\033[m')
sleep(2)
print('O número que eu pensei foi {}{}'.format('\033[33m', nc))
print('\033[32mVoce acertou carai!!' if nu == nc else '\033[31mERRRRRROOOOUUUUU')
