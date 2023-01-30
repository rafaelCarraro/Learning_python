def fatorial(num=0):
    """
    -> Calculate Factorial of any number
    :param num: Number to be calculated
    :return: the result of num's factorial
    made by a communist nobudy
    """
    f = 1
    for c in range(1, num+1):
        f *= c
    return f


def dobro(num=0):
    return num * 2


def triplo(num=0):
    return num * 3