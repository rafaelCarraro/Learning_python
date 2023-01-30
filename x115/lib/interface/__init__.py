def linha(tam=42):
    return '-' * tam


def menu(titulo):
    print(linha())
    print(f'{titulo:^40}')
    print(linha())


def options(vetor):
    menu('MENU PRINCIPAL')
    c = 1
    for item in vetor:
        print(f'\033[1;33m{c} - \033[1;34m{item}\033[m')
        c += 1
    print(linha())
    op = leian('\033[1;33mSua Opção: \033[m')
    return op

def leian(msg):
    while True:
        try:
            n = int(input(msg))
            if 0 >= n or n >= 4:
                print('\033[1;31mValor incorreto, Digite novamente.\033[m')
                continue
        except KeyboardInterrupt:
            print(f'\n\033[1;31mERRO! O usuário deixou o programa sem digitar uma resposta.\033[m')
            return 3
        except (TypeError, ValueError):
            print('\033[1;31mValor incorreto, Digite novamente\033[m')
            continue
        else:
            return n
