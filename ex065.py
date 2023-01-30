#varios num, pergunta a cada se quer continuar, média entre todos, o maio e o menor,
r = str(input('Vamos fazer umas contas?? [S/N] ')).strip()
m = c = s = maior = 0
menor = 100000000000000000000000000000000000
while r not in 'nN':
    n = int(input('Digite um número: '))
    s += n
    c += 1
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    r = str(input('Deseja continuar?? [S/N] ')).strip()
m = s/c
print('Dentre os {} números, a média é {:.2f}, o maior é {}, já o menor {}'.format(c, m, maior, menor))
