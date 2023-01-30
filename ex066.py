c = s = m = 0
print('Vamos brincar, quando quiser parar digite 999')
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    c += 1
    s += n
m = s / c
print(f'Você digitour {c} números, cuja soma é {s} e a média {m:.2f}')
