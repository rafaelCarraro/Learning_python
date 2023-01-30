from time import sleep
#comparar 2 numeros
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número '))
print('Vamos verificar agora:')
sleep(1.2)
if n1 > n2:
    print('{} é maior que {}'.format(n1, n2))
elif n1 < n2:
    print('{} é menor que {}'. format(n1, n2))
elif n1 == n2:
    print('Estes números são inguais')