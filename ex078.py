n = []
mp = mg = cop = cog = 0
for c in range(0, 5):
    n.append(int(input("Digite um valor: ")))
    if c == 0:
        mp = n[c]
        cop = c
    elif mp > n[c]:
        mp = n[c]
        cop = c
    elif mg < n[c]:
        mg = n[c]
        cog = c
print(f'Esta é a lista com os números digitados\n {n}')
print(f'O maior número digitado foi {mg}, na posição: ', end='')
for i, v in enumerate(n):
    if v == mg:
        print(f'{i}...', end='')
print(f'\nO maior número digitado foi {mg}, na posição:', end=' ')
for x, y in enumerate(n):
    if y == mp:
        print(f'{x}...', end='')
