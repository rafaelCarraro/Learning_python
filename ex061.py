#redo 51 com while
i = int(input('Digite o primeiro termo da progressão: '))
r = int(input('Digite a razão da minha vida: '))
c = 1
while c < 10:
    print(i, end='|')
    i += r
    c += 1
print('FIMM')
'''for x in range(0, 10):
    print(i, end='|')
    i += r'''