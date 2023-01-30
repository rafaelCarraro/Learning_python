#same as 61 but asking and showing the next 'n', until shows 0
i = int(input('Digite o primeiro termo da progressão: '))
r = int(input('Digite a razão da minha vida: '))
c = 10
while c != -1:
    print(i, end='|')
    i += r
    c -= 1
    if c == 0:
        c = int(input('\nQuantos mais você deseja ver? \nPara parar digite [999]: '))
        if c == 999:
            break
print('FIMM')