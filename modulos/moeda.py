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
