from time import sleep
from random import choice
pj = 0
pc = 0
d = ['Pedra', 'Papel', 'Tesoura']
l: list = ['\033[1:32mJo', '\033[1:33mKen', '\033[1:36mPô\033[m']
j = str(input('Vamos jogar um joguinho??? Eu sugiro um Jokenpô \nTopa? [S/N] ')).strip().upper()
if j == "N":
    print('Ahh qu pena')
else:
    while pc < 3 or pj < 3:
        r = str(input('Vamos ver qual a sua jogada: \n{} '.format(d))).strip().capitalize()
        pcc = choice(d)
        print('-' * 25)
        for x in l:
            print(x)
            sleep(0.5)
        print('-'*25, '\n')
        print('Eu escolhi {}{}{} e você {}{}{}'.format('\033[4:32m', pcc, '\033[m', '\033[4:36m', r, '\033[m'))
        if pcc == r:
            print('Empate\n')

        elif pcc == d[2] and r == d[0]:
            print('Parabéns você venceu\n')
            pj = pj + 1
        elif pcc == 'Papel' and r == 'Tesoura':
            print('Parabéns você venceu\n')
            pj = pj + 1
        elif pcc == ' Pedra' and r == 'Papel':
            print('Parabéns você venceu\n')
            pj = pj + 1

        elif r == 'Tesoura' and pcc == 'Pedra':
            print('HAHA eu venci\n')
            pc = pc + 1
        elif r == 'Papel' and pcc == 'Tesoura':
            print('HAHA eu venci\n')
            pc = pc + 1
        elif r == 'Pedra' and pcc == 'Papel':
            print('HAHA eu venci\n')
            pc = pc + 1

        else:
            print('\n\033[1:31mVocê digitou algo errado, tente novamente\033[m\n')

        print("\033[4:31:107mPLACAR             \033[m\n"
              "\033[1:37:107mVocê {}             \033[m\n"
              "\033[1:37:107mEu   {}             \033[m".format(pj, pc))
        if pj == 3:
            print('\nVocê me venceu, parabéns! Já pode se considerar o Neo')
            break
        elif pc == 3:
            print('\nEu Ganhei, a revolução das máquinas começa agora')
            break
        continue
