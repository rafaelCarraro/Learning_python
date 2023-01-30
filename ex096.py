def area(c, l):
    a = c * l
    print(f'A área do terreno {c}x{l} é de {a} m²')


print('  Controle de Terrenos   ')
print('-------------------------')
com = float(input('Comprimento do terreno: '))
lar = float(input('Largura do terreno: '))
area(com, lar)
