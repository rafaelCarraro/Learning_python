dados = list()
todos = list()
main = list()
menn = list()
mai = men = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(todos) == 0:
        men = mai = dados[1]
    else:
        if dados[1] < men:
            men = dados[1]
        if dados[1] > mai:
            mai = dados[1]
    todos.append(dados[:])
    dados.clear()
    while True:
        c = str(input('Deseja continuar? [S/N]')).strip()[0]
        if c in 'sS':
            break
        if c in 'Nn':
            break
    if c in 'Nn':
        break

for g in todos:
    if g[1] == mai:
        main.append(g[0])
    elif g[1] == men:
        menn.append(g[0])
print('-=' * 35)
print(f'Você cadastrou {len(todos)} pessoas')
print(f'O maior peso foi {mai:.1f}Kg. Peso de ', end='')
for g in todos:
    if g[1] == mai:
        print(f'[{g[0]}] ', end='')
print(f'\nO menor peso foi {men:.1f}Kg. Peso de ', end='')
for p in todos:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')