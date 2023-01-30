c = r = 0
while True:
    n = int(input('Quer ver a tabuada de qual valor: '))
    if n < 0:
        break
    else:
        c = 0
        print('-' * 21)
        while c < 10:
            c += 1
            print(f'{n} X {c:^2} = {n * c:>2}')
        print('-' * 21)
print('THE END, BITCHES')