def fatorial(num=0, show=False):
    """
    -> Calculate Factorial of any number
    :param num: Number to be calculated
    :param show: (option) to show or not the maths
    :return: the result of num's factorial
    made by a communist nobudy
    """
    f = 1
    print('-' * 30)
    for c in range(num, 0, -1):
        if show:
            print(f' {c} ', end='x')
        f *= c
    if show:
        return f'\b= {f}'
    if not show:
        return f'Sua resposta é {f}'


print(fatorial(5, True))
