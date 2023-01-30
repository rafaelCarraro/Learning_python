c = vi = d = u = v0 = s = 0
print('-' * 28)
print('Insira seu cartão comunista')
print('-' * 28)
v0 = int(input('Já que no comunismo todo mundo que trabalha tem dinheiro \nQuanto deseja sacar? R$ '))
v = v0
ced = 50
while True:
    if v >= ced:
        v -= ced
        c += 1
    else:
        print(f'Total de {c} cedulas de R${ced}')
        if ced == 50:
            ced == 20
        elif ced == 20:
            ced == 10
        elif ced == 10:
            ced == 1
        if v == 0:
            break
    '''elif 20 > v > 10:
        v -= 10
        d += 1
    elif 10 > v > 1:
        v -= 1
        u += 1
s = c + vi + d + u
print("Para o saque de R${:.2}, foram necessárias {} cédulas, sendo:".format(v0, s))
print(f'{c} cédulas de R$50.00')
print(f'{vi} cédulas de R$20.00')
print(f'{d} cédulas de R$10.00')
print(f"{u} cédulas de R$1.00")'''
