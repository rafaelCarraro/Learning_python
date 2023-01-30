mv = 0
hv = 0
ig = 0
nhv = ' '
for c in range(1, 5):
    nome = str(input("Digite o da nome {}º pessoa: ".format(c)))
    i = int(input('Digite a idade dela: '))
    s = int(input('Qual genero se identifica: [1] Femenino [2] Masculino '))
    print('--' * 20)
    ig = i + ig
    if c == 1 and s == 2:
        hv = i
        nhv = nome
    elif s == 2 and hv < i:
        hv = i
        nhv = nome
    elif s == 1 and i < 20:
        mv += 1
m = ig / 4
print('A média de idades é de: {}'.format(m))
print('O homem mais velho é {} com {} anos'.format(nhv.upper(), hv))
print('E são {} o número de mulheres com menos de 20 anos'.format(mv))

