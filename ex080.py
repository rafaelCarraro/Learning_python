ln = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if len(ln) == 0 or n >= ln[-1]:
        ln.append(n)
        print('Adcionado ao final da lista')
    else:
        for x in range(0, len(ln)):
            if n <= ln[x]:
                ln.insert(x, n)
                print(f'Adcionado a posição {x} da  lista')
                break
print('-=' * 35)
print(f'E os valores adcionados em ordem são: {ln}')
