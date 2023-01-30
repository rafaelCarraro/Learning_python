n = s = q = 0
print('Some qualquer quantidade de objetos, para para digite 999')
n = int(input('Digite um número: '))
while n != 999:
    s += n
    q += 1
    n = int(input('Digite um número: '))
print('A soma de {} números foi de {}'.format(q, s))
