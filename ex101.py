from datetime import date


def voto(n=0):
    from datetime import date
    i = date.today().year - n
    if i <= 15:
        return f'Com {i} anos: VOTO NEGADO'
    elif 15 < i < 18 or i >= 65:
        return f'Com {i} anos: VOTO OPCIONAL'
    else:
        return f'Com {i} anos: VOTO OBRIGATORIO'


print('-' * 25)
ano = int(input("Em que ano você nasceu: "))
print(voto(ano))
