from datetime import date
h = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    d = int(input('Data de Nascimento da {}º pessoa: '.format(c)))
    v = h - d
    if v >= 18:
        maior = maior + 1
    else:
        menor = menor + 1
print('Dentre estas pessoas {} são maiores de 18, e {} pessoas são menores de idade'.format(maior, menor))
