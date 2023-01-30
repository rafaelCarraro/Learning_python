s = float(input('Qual o salário do proletáriado? '))
a = s * 1.15
print('faz o {}L{} que agora teu salário é de: R${:.2f}'.format('\033[1;31m','\033[m', a))

