from random import randint
jc = ju = s = c = co = 0
pi = rpi = ''
print('=-' * 16)
print('Vamos jogar Par ou Impar')
print('=-'*16)
while True:
    pi = str(input('Par ou Ímpar? [P/I] '))
    ju = int(input('Qual a sua jogada? '))
    jc = randint(0, 10)
    s = ju + jc
    c = (ju + jc) % 2
    if c == 0:
        rpi = 'par'
    elif c == 1:
        rpi = 'impar'
    print('-' * 48)
    print(f'Você jogou {ju}, e eu {jc}. A soma foi {s} que é {rpi}')
    print('-' * 48)
    if pi in rpi[0]:
        co += 1
        print('Você venceu!!')
        print('Vamos jogar novamente')
    else:
        print(f'GAME OVER, Você venceu {co} vezes')
        break
