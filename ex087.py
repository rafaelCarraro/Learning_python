soma = stc = ssl = 0
matriz = [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
for c, v in enumerate(matriz):
    for x in range(0, 3):
        n = int(input(f'Digite um valor para [{c}, {x}]:'))
        matriz[c][x] = n
        if n % 2 == 0:
            soma += n
        if x == 2:
            stc += n
print('-=' * 25)
for l in range(0, 3):
    for p in range(0, 3):
        print(f'[{matriz[l][p]:^4}]', end='')
    print()
print('-=' * 25)
print(f'A soma de todos os valores pares é: {soma}')
print(f'A soma da terceira coluna resulta em: {stc} ')
print(f'E o maior valor encontrado na senguda linha foi: {max(matriz[1])} ')