print('Para verificar se a frase é um Palíndromo')
f = str(input('Digite uma frase: ')).lower()
lis = []
los = []
for x in range(0, len(f)):
    if f[x] != ' ':
        lis.insert(0, f[x])
        los.append(f[x])
print('A frase', end=', ')
[print(y, end='')for y in lis]
print('\ninvertida, fica', end=': ')
[print(z, end='') for z in los]
if lis == los:
    print('\n\nÉ um palindromooooo, finalmente')
else:
    print('\nNão é um palindromo, e eu não sei porque voce que saber disso')

p = f.split()
j = ''.join(p)
i = ''
for l in range(len(j)-1, -1, -1):
    i += j[l]
if i == j:
    print('temos um palindromo')
else:
    print('Ablublabla')