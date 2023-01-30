tu = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
n = 20
while True:
    n = int(input("Digite um número de 0 a 10 "))
    if n > 20:
        if n < 0:
            n *= -1
            print(f'Você quis dizer {n}?')
        print(tu[n])