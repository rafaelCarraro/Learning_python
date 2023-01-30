def leiaint(num=''):
    while True:
        if not num.isnumeric():
            print(f'\033[1;31mERRO! Digite um número inteiro válido.\033[m')
            num = input('Digite um número: ')
        else:
            return num
            break

n = leiaint(input('Digite um número: ')).lower()
print(f'Você acabou de digitar o número {n}')
