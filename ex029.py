import emoji
v = int(input('A qual velocidade você está dirigindo? '))
print('A velocidade da pista é de 80km/h, e voce está a {}km/h'.format(v))
if v > 80:
    print(emoji.emojize(':police:\033[31mVocê está recebendo uma multa de \033[33mR$ {:.2f}:police_car:'
                        .format((v - 80) * 7), language='alias'))
else:
    print('\033[32mBoa Capião, segue na maciota pra não se fuder')
