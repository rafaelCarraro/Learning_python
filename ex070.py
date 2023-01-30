t = pc = c = 0
npb = ''
pb = 1000000000000000000000000
print('-' * 25)
print('   LOJA SUPER BARATÃO   ')
print('-' * 25)
while True:
    n = str(input('Nome do Produto: '))
    p = float(input('Preço: R$ '))
    c += 1
    t += p
    if p > 1000:
        pc += 1
    elif pb >    p:
        pb = p
        npb = n
    co = str(input('Deseja continuar? [S/N]'))
    while co not in "sSnN":
        co = str(input('Deseja continuar? [S/N]'))
    if co in 'Nn':
        print('----Fim do Programa----')
        break
print(f'O total de {c} items foi R${t:.2f};')
print(f'Você comprou {pc} produtos acima de R$1000,00;')
print(f'O produto mais barato foi {npb}, que custa R${pb:.2f}')
