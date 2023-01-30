def resumo(num=0, pa=0, pd=0):
    print('-'*26)
    print(f'     RESUMO DE VALOR   ')
    print('-'*26)
    print(f'Preço analisado:   {moeda(num): <8}')
    print(f'Dobro do preço:    {dobro(num): <8}')
    print(f'Metade do preço:   {metade(num): <8}')
    print(f'{pa}% de aumento:    {aumentar(num, pa): <8}')
    print(f'{pd}% de desconto:   {diminuir(num, pd): <8}')


def aumentar(c=0, p=0, k=True):
    c += c * (p / 100)
    if k:
        return moeda(c)
    else:
        return c


def diminuir(c=0, p=0, k=True):
    c -= c * (p / 100)
    if k:
        return moeda(c)
    else:
        return c


def metade(num=0, k=True):
    if k:
        return moeda(num / 2)
    else:
        return num / 2


def dobro(num=0, k= True):
    if k:
        return moeda(num * 2)
    else:
        return num * 2


def moeda(num=0, coin='R$'):
    return f'{coin}{num:<.2f}'.replace('.', ',')
