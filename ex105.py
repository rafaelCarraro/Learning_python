def notas(*n, sit=False):
    """
    -> To analyze grades returning total, greater, worst, average and situation
    :param n: one or more grades
    :param sit: (option): to return or not the situation
    :return: dict with named keys and respectively values.
    made by a communist nobody
    """
    d = {'total': len(n),
         'Maior': max(n),
         'Menor': min(n),
         'Média': sum(n) / len(n)}
    if sit:
        if d['Média'] >= 7:
            d['Situação'] = 'BOA'
        elif 7 > d['Média'] >= 5:
            d['Situação'] = 'Razoável'
        else:
            d['Situação'] = 'RUIM'
    return d

resp = notas(5.5, 2.5, 10, 6.5, sit=True)
print(resp)
