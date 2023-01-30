p = float(input('Valor do produto: '))
print('Qual a forma de pagamento\n a) Dinheiro ou Cheque\n '
              'b) Cartão\n c) até 2X\n d) mais de 3X\n')
f = str(input('Sua opção: ')).strip().upper()
if f == 'A':
    t = p * 0.1
    print('O valor final foi de R${:.2f} devido ao desconto'.format(p-t))
elif f == 'B':
    t = p * 0.05
    print('O valor final ficou em R${:.2f} devido ao desconto'.format(p-t))
elif f == 'D':
    t = p * 0.2
    print('O valor final teve um acréssimo e ficou em R${:.2f}'.format(t+p))
else:
    print('O valor total de sua compra é de R${:.2f}'.format(p))