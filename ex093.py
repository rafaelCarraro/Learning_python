saporra = {}
lg = []
soma = 0
saporra['nome'] = str(input('Nome do jogador: '))
p = int(input(f'Quantas partidas {saporra["nome"]} jogou: '))
for x in range(1, p + 1):
    g = int(input(f'Quantos gols na partida {x}: '))
    lg.append(g)
    soma += g
saporra['gols'] = lg
saporra['total'] = soma
print('-=' * 35)
print(saporra)
print('-=' * 35)
for k, v in saporra.items():
    print(f'O campo {k} tem valor {v}.')
print('-=' * 35)
print(f"O jogador {saporra['nome']} jogou {p} partidas.")
for c in range(0, len(lg)+1):
    print(f'    ==> Na partida {c+1}, fez {lg[c]} gols.')
print(f'Foi um total de {saporra["total"]} gols.')
