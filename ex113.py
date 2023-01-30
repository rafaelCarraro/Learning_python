def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[0;31mERRO!! Digite um número inteiro válido. \033[m')
            continue
        except KeyboardInterrupt:
            print(f'\033[0;31mERRO! O usuário deixou o programa sem digitar uma resposta.\033[m')
            return 0
        else:
            return num

def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print(f'\033[0;31mERRO!! Digite um número real válido. \033[m')
            continue
        except KeyboardInterrupt:
            print(f'\033[0;31mERRO! O usuário deixou o programa sem digitar uma resposta.\033[m')
            return 0
        else:
            return num


n = leiaInt('Digite um número inteiro: ')
n2 = leiaFloat('Digite um número real: ')
print(f'Você digitou o valor inteiro {n} e o valor real {n2}.')
